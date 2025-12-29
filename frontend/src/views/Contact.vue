<template>
  <div class="contact-page">
    <div class="page-header">
      <div class="container">
        <h1>联系我们</h1>
        <p>期待与您的合作</p>
      </div>
    </div>

    <section class="contact-content">
      <div class="container">
        <div class="contact-grid">
          <div class="contact-info">
            <h2>联系方式</h2>
            
            <div class="info-item">
              <div class="info-icon">📞</div>
              <div class="info-text">
                <h4>服务热线</h4>
                <p>400-826-1128</p>
              </div>
            </div>

            <div class="info-item">
              <div class="info-icon">📧</div>
              <div class="info-text">
                <h4>公司邮箱</h4>
                <p>sales@chinatuta.com</p>
              </div>
            </div>

            <div class="info-item">
              <div class="info-icon">📍</div>
              <div class="info-text">
                <h4>公司地址</h4>
                <p>浙江省台州市椒江区海韵路528号</p>
              </div>
            </div>

            <div class="info-item">
              <div class="info-icon">📮</div>
              <div class="info-text">
                <h4>邮政编码</h4>
                <p>318000</p>
              </div>
            </div>
          </div>

          <div class="contact-form card">
            <h2>在线咨询</h2>
            <el-form :model="form" label-position="top">
              <el-form-item label="姓名">
                <el-input v-model="form.name" placeholder="请输入您的姓名" />
              </el-form-item>
              
              <el-form-item label="联系电话">
                <el-input v-model="form.phone" placeholder="请输入您的联系电话" />
              </el-form-item>
              
              <el-form-item label="电子邮箱">
                <el-input v-model="form.email" type="email" placeholder="请输入您的电子邮箱" />
              </el-form-item>
              
              <el-form-item label="咨询内容">
                <el-input 
                  v-model="form.message" 
                  type="textarea" 
                  :rows="5"
                  placeholder="请输入您的咨询内容"
                />
              </el-form-item>
              
              <el-button type="primary" class="submit-button" @click="submitForm">
                提交咨询
              </el-button>
            </el-form>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { ElMessage } from 'element-plus'

const form = reactive({
  name: '',
  phone: '',
  email: '',
  message: ''
})

const submitForm = () => {
  if (!form.name || !form.phone || !form.message) {
    ElMessage.warning('请填写完整信息')
    return
  }
  
  ElMessage.success('提交成功，我们会尽快与您联系！')
  
  // 清空表单
  form.name = ''
  form.phone = ''
  form.email = ''
  form.message = ''
}
</script>

<style lang="scss" scoped>
.page-header {
  background: linear-gradient(135deg, #2CB5BE 0%, #1a8a91 100%);
  color: white;
  padding: 80px 0;
  text-align: center;

  h1 {
    font-size: 48px;
    margin-bottom: 15px;
  }

  p {
    font-size: 20px;
    opacity: 0.9;
  }
}

.contact-content {
  padding: 80px 0;
  background: #f8f9fa;

  .contact-grid {
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    gap: 60px;
    align-items: start;
  }

  .contact-info {
    h2 {
      font-size: 28px;
      color: #333;
      margin-bottom: 40px;
    }

    .info-item {
      display: flex;
      align-items: flex-start;
      gap: 20px;
      margin-bottom: 30px;
      padding: 20px;
      background: white;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);

      .info-icon {
        font-size: 32px;
        flex-shrink: 0;
      }

      .info-text {
        h4 {
          font-size: 16px;
          color: #333;
          margin-bottom: 8px;
        }

        p {
          font-size: 15px;
          color: #666;
          margin: 0;
        }
      }
    }
  }

  .contact-form {
    padding: 40px;
    background: white;

    h2 {
      font-size: 28px;
      color: #333;
      margin-bottom: 30px;
    }

    .submit-button {
      width: 100%;
      height: 45px;
      background: #2CB5BE;
      border-color: #2CB5BE;
      font-size: 16px;
      
      &:hover {
        background: #1a8a91;
        border-color: #1a8a91;
      }
    }
  }
}

@media (max-width: 768px) {
  .contact-content .contact-grid {
    grid-template-columns: 1fr;
  }
}
</style>

