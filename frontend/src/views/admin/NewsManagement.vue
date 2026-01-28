<template>
  <div class="news-management">
    <div class="page-header">
      <h1>新闻资讯管理</h1>
      <el-button type="primary" @click="openCreateDialog">
        <el-icon><Plus /></el-icon>
        新建新闻
      </el-button>
    </div>

    <!-- 筛选栏 -->
    <div class="filters">
      <el-select v-model="filterCategory" placeholder="选择分类" clearable @change="loadNewsList">
        <el-option label="全部分类" value="" />
        <el-option label="公司新闻" value="company" />
        <el-option label="展会现场" value="exhibition" />
      </el-select>

      <el-select v-model="filterStatus" placeholder="发布状态" clearable @change="loadNewsList">
        <el-option label="全部状态" value="" />
        <el-option label="已发布" value="published" />
        <el-option label="草稿" value="draft" />
      </el-select>
    </div>

    <!-- 新闻列表表格 -->
    <el-table v-loading="loading" :data="newsList" stripe>
      <el-table-column label="ID" width="100">
        <template #default="{ row }">
          <span class="uuid-cell" :title="row.id">{{ row.id.slice(0, 8) }}...</span>
        </template>
      </el-table-column>
      <el-table-column label="封面图" width="120">
        <template #default="{ row }">
          <el-image 
            v-if="row.image_url" 
            :src="row.image_url" 
            fit="cover"
            style="width: 80px; height: 50px; border-radius: 4px;"
          />
          <span v-else class="no-image">暂无图片</span>
        </template>
      </el-table-column>
      <el-table-column prop="title" label="标题" min-width="200">
        <template #default="{ row }">
          <span class="news-title">{{ row.title }}</span>
        </template>
      </el-table-column>
      <el-table-column label="分类" width="100">
        <template #default="{ row }">
          <el-tag :type="row.category === 'company' ? 'primary' : 'warning'" size="small">
            {{ row.category === 'company' ? '公司新闻' : '展会现场' }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="状态" width="90">
        <template #default="{ row }">
          <el-tag :type="row.status === 'published' ? 'success' : 'info'" size="small">
            {{ row.status === 'published' ? '已发布' : '草稿' }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="发布时间" width="160">
        <template #default="{ row }">
          {{ row.published_at ? formatDate(row.published_at) : '-' }}
        </template>
      </el-table-column>
      <el-table-column label="更新时间" width="160">
        <template #default="{ row }">
          {{ formatDate(row.updated_at) }}
        </template>
      </el-table-column>
      <el-table-column label="操作" width="280" fixed="right">
        <template #default="{ row }">
          <el-button size="small" @click="handlePreview(row)">
            <el-icon><View /></el-icon>
            预览
          </el-button>
          <el-button size="small" type="primary" @click="handleEdit(row)">
            <el-icon><Edit /></el-icon>
            编辑
          </el-button>
          <el-button 
            v-if="row.status === 'draft'" 
            size="small" 
            type="success" 
            @click="handlePublish(row)"
          >
            发布
          </el-button>
          <el-button 
            v-else 
            size="small" 
            type="warning" 
            @click="handleUnpublish(row)"
          >
            撤回
          </el-button>
          <el-button size="small" type="danger" @click="handleDelete(row)">
            <el-icon><Delete /></el-icon>
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 空状态 -->
    <el-empty v-if="!loading && newsList.length === 0" description="暂无新闻" />

    <!-- 新建/编辑对话框 -->
    <el-dialog 
      v-model="dialogVisible" 
      :title="isEdit ? '编辑新闻' : '新建新闻'" 
      width="700px"
      :close-on-click-modal="false"
    >
      <el-form 
        ref="formRef" 
        :model="formData" 
        :rules="formRules" 
        label-width="80px"
      >
        <el-form-item label="标题" prop="title">
          <el-input v-model="formData.title" placeholder="请输入新闻标题" maxlength="100" show-word-limit />
        </el-form-item>

        <el-form-item label="分类" prop="category">
          <el-select v-model="formData.category" placeholder="请选择分类">
            <el-option label="公司新闻" value="company" />
            <el-option label="展会现场" value="exhibition" />
          </el-select>
        </el-form-item>

        <el-form-item label="封面图">
          <div class="image-upload-area">
            <div v-if="formData.image_url" class="image-preview">
              <el-image :src="formData.image_url" fit="cover" />
              <el-button class="remove-btn" type="danger" circle size="small" @click="formData.image_url = ''">
                <el-icon><Close /></el-icon>
              </el-button>
            </div>
            <el-upload
              v-else
              ref="uploadRef"
              :auto-upload="true"
              :show-file-list="false"
              :action="uploadUrl"
              :headers="uploadHeaders"
              :data="{ category: 'news' }"
              :on-success="handleUploadSuccess"
              :on-error="handleUploadError"
              :before-upload="beforeUpload"
              accept="image/*"
            >
              <div class="upload-placeholder">
                <el-icon class="upload-icon"><Plus /></el-icon>
                <span>点击上传封面图</span>
              </div>
            </el-upload>
          </div>
        </el-form-item>

        <el-form-item label="摘要" prop="summary">
          <el-input 
            v-model="formData.summary" 
            type="textarea" 
            :rows="3" 
            placeholder="请输入新闻摘要" 
            maxlength="300" 
            show-word-limit 
          />
        </el-form-item>

        <el-form-item label="正文" prop="content">
          <el-input 
            v-model="formData.content" 
            type="textarea" 
            :rows="8" 
            placeholder="请输入新闻正文内容" 
          />
        </el-form-item>
      </el-form>

      <template #footer>
        <div class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="info" @click="handleSaveAndPreview" :loading="saving">
            保存并预览
          </el-button>
          <el-button type="primary" @click="handleSave" :loading="saving">
            保存
          </el-button>
        </div>
      </template>
    </el-dialog>

    <!-- 预览对话框提示 -->
    <el-dialog v-model="previewDialogVisible" title="预览链接" width="500px">
      <div class="preview-info">
        <p>预览链接已生成（永久有效）：</p>
        <el-input v-model="previewUrl" readonly>
          <template #append>
            <el-button @click="copyPreviewUrl">复制</el-button>
          </template>
        </el-input>
      </div>
      <template #footer>
        <el-button @click="previewDialogVisible = false">关闭</el-button>
        <el-button type="primary" @click="openPreviewInNewTab">
          <el-icon><View /></el-icon>
          在新窗口预览
        </el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed } from 'vue'
import axios from '@/utils/axios'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Plus, Edit, Delete, View, Close } from '@element-plus/icons-vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()

const loading = ref(false)
const saving = ref(false)
const dialogVisible = ref(false)
const previewDialogVisible = ref(false)
const isEdit = ref(false)
const newsList = ref([])
const filterCategory = ref('')
const filterStatus = ref('')
const formRef = ref(null)
const previewUrl = ref('')
const editingId = ref(null)

// 上传配置
const uploadUrl = '/api/v1/media/upload'
const uploadHeaders = computed(() => ({
  Authorization: `Bearer ${authStore.token}`
}))

const formData = reactive({
  title: '',
  summary: '',
  content: '',
  image_url: '',
  category: 'company'
})

const formRules = {
  title: [{ required: true, message: '请输入新闻标题', trigger: 'blur' }],
  category: [{ required: true, message: '请选择分类', trigger: 'change' }]
}

// 格式化日期
const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  })
}

// 加载新闻列表
const loadNewsList = async () => {
  loading.value = true
  try {
    const params = {}
    if (filterCategory.value) params.category = filterCategory.value
    if (filterStatus.value !== '') params.status = filterStatus.value

    const response = await axios.get('/api/v1/news/admin/list', { params })
    newsList.value = response.data
  } catch (error) {
    ElMessage.error('加载新闻列表失败')
  } finally {
    loading.value = false
  }
}

// 打开新建对话框
const openCreateDialog = () => {
  isEdit.value = false
  editingId.value = null
  Object.assign(formData, {
    title: '',
    summary: '',
    content: '',
    image_url: '',
    category: 'company'
  })
  dialogVisible.value = true
}

// 编辑新闻
const handleEdit = (row) => {
  isEdit.value = true
  editingId.value = row.id
  Object.assign(formData, {
    title: row.title,
    summary: row.summary || '',
    content: row.content || '',
    image_url: row.image_url || '',
    category: row.category
  })
  dialogVisible.value = true
}

// 保存新闻
const handleSave = async () => {
  const valid = await formRef.value.validate().catch(() => false)
  if (!valid) return

  saving.value = true
  try {
    if (isEdit.value) {
      await axios.put(`/api/v1/news/${editingId.value}`, formData)
      ElMessage.success('新闻更新成功')
    } else {
      await axios.post('/api/v1/news', formData)
      ElMessage.success('新闻创建成功')
    }
    dialogVisible.value = false
    await loadNewsList()
  } catch (error) {
    ElMessage.error(error.response?.data?.detail || '保存失败')
  } finally {
    saving.value = false
  }
}

// 保存并预览
const handleSaveAndPreview = async () => {
  const valid = await formRef.value.validate().catch(() => false)
  if (!valid) return

  saving.value = true
  try {
    let newsId
    if (isEdit.value) {
      await axios.put(`/api/v1/news/${editingId.value}`, formData)
      newsId = editingId.value
    } else {
      const response = await axios.post('/api/v1/news', formData)
      newsId = response.data.id
    }

    // 生成预览令牌
    const previewResponse = await axios.post(`/api/v1/news/${newsId}/preview`)
    previewUrl.value = window.location.origin + previewResponse.data.preview_url
    
    dialogVisible.value = false
    previewDialogVisible.value = true
    await loadNewsList()
  } catch (error) {
    ElMessage.error(error.response?.data?.detail || '保存失败')
  } finally {
    saving.value = false
  }
}

// 预览新闻
const handlePreview = async (row) => {
  try {
    const response = await axios.post(`/api/v1/news/${row.id}/preview`)
    previewUrl.value = window.location.origin + response.data.preview_url
    previewDialogVisible.value = true
  } catch (error) {
    ElMessage.error('生成预览链接失败')
  }
}

// 复制预览链接
const copyPreviewUrl = () => {
  navigator.clipboard.writeText(previewUrl.value).then(() => {
    ElMessage.success('链接已复制')
  }).catch(() => {
    ElMessage.error('复制失败')
  })
}

// 在新窗口打开预览
const openPreviewInNewTab = () => {
  window.open(previewUrl.value, '_blank')
}

// 发布新闻
const handlePublish = async (row) => {
  try {
    await ElMessageBox.confirm('确定要发布这条新闻吗？', '提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'info'
    })

    await axios.post(`/api/v1/news/${row.id}/publish`)
    ElMessage.success('新闻已发布')
    await loadNewsList()
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('发布失败')
    }
  }
}

// 撤回发布
const handleUnpublish = async (row) => {
  try {
    await ElMessageBox.confirm('确定要撤回这条新闻吗？撤回后将变为草稿状态。', '提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    })

    await axios.post(`/api/v1/news/${row.id}/unpublish`)
    ElMessage.success('新闻已撤回')
    await loadNewsList()
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('撤回失败')
    }
  }
}

// 删除新闻
const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除新闻"${row.title}"吗？此操作不可恢复。`, '警告', {
      confirmButtonText: '删除',
      cancelButtonText: '取消',
      type: 'warning'
    })

    await axios.delete(`/api/v1/news/${row.id}`)
    ElMessage.success('新闻已删除')
    await loadNewsList()
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败')
    }
  }
}

// 上传前检查
const beforeUpload = (file) => {
  const isImage = file.type.startsWith('image/')
  const isLt5M = file.size / 1024 / 1024 < 5

  if (!isImage) {
    ElMessage.error('只能上传图片文件')
    return false
  }
  if (!isLt5M) {
    ElMessage.error('图片大小不能超过 5MB')
    return false
  }
  return true
}

// 上传成功
const handleUploadSuccess = (response) => {
  formData.image_url = response.file_url
  ElMessage.success('图片上传成功')
}

// 上传失败
const handleUploadError = () => {
  ElMessage.error('图片上传失败')
}

onMounted(() => {
  loadNewsList()
})
</script>

<style lang="scss" scoped>
.news-management {
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
      width: 150px;
    }
  }

  .uuid-cell {
    font-family: monospace;
    font-size: 12px;
    color: #666;
    cursor: help;
  }

  .news-title {
    font-weight: 500;
    color: #333;
  }

  .no-image {
    color: #999;
    font-size: 12px;
  }

  .image-upload-area {
    .image-preview {
      position: relative;
      width: 200px;
      height: 120px;
      border-radius: 8px;
      overflow: hidden;

      .el-image {
        width: 100%;
        height: 100%;
      }

      .remove-btn {
        position: absolute;
        top: 8px;
        right: 8px;
      }
    }

    .upload-placeholder {
      width: 200px;
      height: 120px;
      border: 2px dashed #dcdfe6;
      border-radius: 8px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.3s;
      color: #909399;

      &:hover {
        border-color: #2CB5BE;
        color: #2CB5BE;
      }

      .upload-icon {
        font-size: 32px;
        margin-bottom: 8px;
      }

      span {
        font-size: 13px;
      }
    }
  }

  .dialog-footer {
    display: flex;
    justify-content: flex-end;
    gap: 12px;
  }

  .preview-info {
    p {
      margin-bottom: 12px;
      color: #666;
    }
  }
}
</style>
