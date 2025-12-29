<template>
  <div class="media-management">
    <div class="page-header">
      <h1>媒体文件管理</h1>
      <el-button type="primary" @click="uploadDialogVisible = true">
        <el-icon><Upload /></el-icon>
        上传文件
      </el-button>
    </div>

    <div class="filters">
      <el-select v-model="filterCategory" placeholder="选择分类" clearable @change="loadMediaFiles">
        <el-option label="全部" value="" />
        <el-option label="产品图片" value="product" />
        <el-option label="新闻图片" value="news" />
        <el-option label="公司相关" value="company" />
        <el-option label="文档资料" value="document" />
      </el-select>

      <el-select v-model="filterType" placeholder="选择类型" clearable @change="loadMediaFiles">
        <el-option label="全部" value="" />
        <el-option label="图片" value="image" />
        <el-option label="文档" value="document" />
        <el-option label="其他" value="other" />
      </el-select>
    </div>

    <div v-loading="loading" class="media-grid">
      <div v-for="file in mediaFiles" :key="file.id" class="media-item">
        <div class="media-preview">
          <img v-if="file.media_type === 'image'" :src="file.file_url" :alt="file.original_filename" />
          <div v-else class="file-icon">
            <el-icon><Document /></el-icon>
          </div>
        </div>
        
        <div class="media-info">
          <div class="media-name" :title="file.original_filename">
            {{ file.original_filename }}
          </div>
          <div class="media-meta">
            <span>{{ formatFileSize(file.file_size) }}</span>
            <span>{{ formatDate(file.created_at) }}</span>
          </div>
        </div>

        <div class="media-actions">
          <el-button size="small" @click="copyUrl(file.file_url)">
            <el-icon><CopyDocument /></el-icon>
          </el-button>
          <el-button size="small" type="danger" @click="handleDelete(file)">
            <el-icon><Delete /></el-icon>
          </el-button>
        </div>
      </div>

      <el-empty v-if="!loading && mediaFiles.length === 0" description="暂无文件" />
    </div>

    <!-- 上传对话框 -->
    <el-dialog v-model="uploadDialogVisible" title="上传文件" width="500px">
      <el-form :model="uploadForm" label-width="80px">
        <el-form-item label="文件分类">
          <el-select v-model="uploadForm.category" placeholder="请选择分类">
            <el-option label="产品图片" value="product" />
            <el-option label="新闻图片" value="news" />
            <el-option label="公司相关" value="company" />
            <el-option label="文档资料" value="document" />
          </el-select>
        </el-form-item>

        <el-form-item label="选择文件">
          <el-upload
            ref="uploadRef"
            :auto-upload="false"
            :on-change="handleFileChange"
            :limit="1"
            drag
          >
            <el-icon class="el-icon--upload"><upload-filled /></el-icon>
            <div class="el-upload__text">
              拖拽文件到此处或<em>点击上传</em>
            </div>
            <template #tip>
              <div class="el-upload__tip">
                支持 jpg/png/gif/pdf/doc/xls 等格式，文件大小不超过 10MB
              </div>
            </template>
          </el-upload>
        </el-form-item>
      </el-form>

      <template #footer>
        <el-button @click="uploadDialogVisible = false">取消</el-button>
        <el-button type="primary" :loading="uploading" @click="handleUpload">
          确认上传
        </el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '@/utils/axios'
import { ElMessage, ElMessageBox } from 'element-plus'
import { UploadFilled } from '@element-plus/icons-vue'

const loading = ref(false)
const uploading = ref(false)
const uploadDialogVisible = ref(false)
const mediaFiles = ref([])
const filterCategory = ref('')
const filterType = ref('')
const selectedFile = ref(null)

const uploadForm = ref({
  category: 'product'
})

const loadMediaFiles = async () => {
  loading.value = true
  try {
    const params = {}
    if (filterCategory.value) params.category = filterCategory.value
    if (filterType.value) params.media_type = filterType.value

    const response = await axios.get('/api/v1/media/list', { params })
    mediaFiles.value = response.data
  } catch (error) {
    ElMessage.error('加载文件列表失败')
  } finally {
    loading.value = false
  }
}

const handleFileChange = (file) => {
  selectedFile.value = file.raw
}

const handleUpload = async () => {
  if (!selectedFile.value) {
    ElMessage.warning('请选择要上传的文件')
    return
  }

  const formData = new FormData()
  formData.append('file', selectedFile.value)
  if (uploadForm.value.category) {
    formData.append('category', uploadForm.value.category)
  }

  uploading.value = true
  try {
    await axios.post('/api/v1/media/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    })
    
    ElMessage.success('文件上传成功')
    uploadDialogVisible.value = false
    selectedFile.value = null
    await loadMediaFiles()
  } catch (error) {
    ElMessage.error(error.response?.data?.detail || '文件上传失败')
  } finally {
    uploading.value = false
  }
}

const handleDelete = async (file) => {
  try {
    await ElMessageBox.confirm(
      `确定要删除文件 "${file.original_filename}" 吗？`,
      '提示',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }
    )

    await axios.delete(`/api/v1/media/${file.id}`)
    ElMessage.success('文件删除成功')
    await loadMediaFiles()
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('文件删除失败')
    }
  }
}

const copyUrl = (url) => {
  const fullUrl = window.location.origin + url
  navigator.clipboard.writeText(fullUrl).then(() => {
    ElMessage.success('URL已复制到剪贴板')
  }).catch(() => {
    ElMessage.error('复制失败')
  })
}

const formatFileSize = (bytes) => {
  if (bytes === 0) return '0 B'
  const k = 1024
  const sizes = ['B', 'KB', 'MB', 'GB']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i]
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('zh-CN')
}

onMounted(() => {
  loadMediaFiles()
})
</script>

<style lang="scss" scoped>
.media-management {
  .page-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;

    h1 {
      font-size: 24px;
      color: #333;
      margin: 0;
    }
  }

  .filters {
    display: flex;
    gap: 15px;
    margin-bottom: 24px;

    .el-select {
      width: 200px;
    }
  }

  .media-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 20px;
    min-height: 300px;
  }

  .media-item {
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    transition: all 0.3s;

    &:hover {
      box-shadow: 0 6px 16px rgba(0, 0, 0, 0.12);
      transform: translateY(-2px);
    }

    .media-preview {
      width: 100%;
      height: 180px;
      background: #f5f5f5;
      display: flex;
      align-items: center;
      justify-content: center;

      img {
        width: 100%;
        height: 100%;
        object-fit: cover;
      }

      .file-icon {
        font-size: 48px;
        color: #999;
      }
    }

    .media-info {
      padding: 12px;

      .media-name {
        font-size: 14px;
        color: #333;
        margin-bottom: 8px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }

      .media-meta {
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        color: #999;
      }
    }

    .media-actions {
      padding: 0 12px 12px;
      display: flex;
      gap: 8px;

      .el-button {
        flex: 1;
      }
    }
  }
}
</style>

