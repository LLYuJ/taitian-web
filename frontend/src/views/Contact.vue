<template>
  <div class="contact-page">
    <!-- 面包屑导航 -->
    <div class="breadcrumb-container">
      <div class="container">
        <nav class="breadcrumb">
          <router-link :to="localePath('/')">{{ t('nav.home') }}</router-link>
          <span class="separator">&gt;</span>
          <span class="current">{{ t('contactPage.title') }}</span>
        </nav>
      </div>
    </div>

    <!-- 页面头部 Banner -->
    <div class="page-header">
      <div class="header-bg-image"></div>
      <div class="header-content">
        <h1>{{ t('contactPage.heroTitle') }}</h1>
        <p>{{ t('contactPage.heroSubtitle') }}</p>
      </div>
    </div>

    <!-- 公司介绍区域 -->
    <section class="company-intro">
      <div class="container">
        <div class="intro-grid">
          <div class="intro-image">
            <img :src="companyImage" alt="泰田集团" />
          </div>
          <div class="intro-content">
            <h2>{{ t('contactPage.companyName') }}</h2>
            <p class="intro-desc">{{ t('contactPage.companyDesc') }}</p>
            <div class="contact-item">
              <img src="@/assets/images/icons/tel.png" alt="电话" class="contact-icon" />
              <span class="contact-text">400-826-1128</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 联系表单区域 -->
    <section class="contact-form-section">
      <div class="container">
        <div class="form-header">
          <h2>{{ t('contactPage.formTitle') }}</h2>
          <p>{{ t('contactPage.formSubtitle') }}</p>
        </div>
        
        <div class="form-content">
          <div class="contact-form">
            <form @submit.prevent="submitForm">
              <div class="form-row">
                <div class="form-group">
                  <label>{{ t('contactPage.form.name') }}</label>
                  <input v-model="form.name" type="text" :placeholder="t('contactPage.form.namePlaceholder')" />
                </div>
                <div class="form-group">
                  <label>{{ t('contactPage.form.company') }} <span class="required">*</span></label>
                  <input v-model="form.company" type="text" :placeholder="t('contactPage.form.companyPlaceholder')" />
                </div>
              </div>
              
              <div class="form-row">
                <div class="form-group">
                  <label>{{ t('contactPage.form.phone') }}</label>
                  <div class="phone-input">
                    <span class="country-code">🇨🇳</span>
                    <input v-model="form.phone" type="tel" :placeholder="t('contactPage.form.phonePlaceholder')" />
                  </div>
                </div>
                <div class="form-group">
                  <label>{{ t('contactPage.form.email') }} <span class="required">*</span></label>
                  <input v-model="form.email" type="email" :placeholder="t('contactPage.form.emailPlaceholder')" />
                </div>
              </div>
              
              <div class="form-group full-width">
                <label>{{ t('contactPage.form.message') }}</label>
                <textarea 
                  v-model="form.message" 
                  rows="5"
                  :placeholder="t('contactPage.form.messagePlaceholder')"
                ></textarea>
              </div>
              
              <button type="submit" class="submit-button">
                {{ t('contactPage.form.submit') }}
              </button>
            </form>
          </div>
          
          <div class="captcha-area">
            <div class="captcha-box">
              <span class="captcha-text">人机</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useLocale } from '@/composables/useLocale'

import companyImg from '@/assets/images/banners/new_factory.png'

const { t, localePath } = useLocale()

const companyImage = ref(companyImg)

const form = reactive({
  name: '',
  company: '',
  phone: '',
  email: '',
  message: ''
})

const submitForm = () => {
  if (!form.company || !form.email) {
    alert(t('contactPage.form.fillComplete'))
    return
  }
  
  alert(t('contactPage.form.submitSuccess'))
  
  // 清空表单
  form.name = ''
  form.company = ''
  form.phone = ''
  form.email = ''
  form.message = ''
}
</script>

<style lang="scss" scoped>
// 面包屑导航
.breadcrumb-container {
  background: #f5f5f5;
  padding: 12px 0;
  border-bottom: 1px solid #e8e8e8;
  
  .breadcrumb {
    display: flex;
    align-items: center;
    font-size: 14px;
    
    a {
      color: #0066cc;
      text-decoration: none;
      
      &:hover {
        text-decoration: underline;
      }
    }
    
    .separator {
      margin: 0 8px;
      color: #999;
    }
    
    .current {
      color: #666;
    }
  }
}

// 页面头部 Banner
.page-header {
  position: relative;
  height: 220px;
  display: flex;
  align-items: center;
  overflow: hidden;
  
  .header-bg-image {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #3EC6CB 0%, #4FD1C5 50%, #5DD3C8 100%);
    z-index: 0;
    
    // 添加Logo水印效果
    &::after {
      content: '';
      position: absolute;
      right: 10%;
      top: 50%;
      transform: translateY(-50%);
      width: 300px;
      height: 300px;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cpath d='M20 80 L20 20 L80 20' stroke='rgba(255,255,255,0.15)' stroke-width='8' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3Cpath d='M30 70 L30 30 L70 30 L70 50' stroke='rgba(255,255,255,0.15)' stroke-width='6' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3Cpath d='M55 45 L75 65' stroke='rgba(255,255,255,0.15)' stroke-width='6' fill='none' stroke-linecap='round'/%3E%3Cpath d='M70 50 L80 60' stroke='rgba(255,255,255,0.15)' stroke-width='4' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
      background-repeat: no-repeat;
      background-size: contain;
      opacity: 0.8;
    }
  }
  
  .header-content {
    position: relative;
    z-index: 2;
    padding-left: 10%;
    color: white;
    
    h1 {
      font-size: 36px;
      font-weight: 600;
      margin-bottom: 16px;
      letter-spacing: 1px;
    }

    p {
      font-size: 16px;
      opacity: 0.95;
      max-width: 600px;
      line-height: 1.8;
    }
  }
}

// 公司介绍区域
.company-intro {
  padding: 60px 0;
  background: #fff;

  .intro-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
  }
  
  .intro-image {
    img {
      width: 100%;
      height: auto;
      border-radius: 4px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
  }
  
  .intro-content {
    h2 {
      font-size: 24px;
      color: #0088cc;
      font-weight: 600;
      margin-bottom: 20px;
    }
    
    .intro-desc {
      font-size: 15px;
      color: #666;
      line-height: 1.8;
      margin-bottom: 30px;
    }
    
    .contact-item {
      display: flex;
      align-items: center;
      gap: 12px;
      
      .contact-icon {
        width: 24px;
        height: 24px;
        object-fit: contain;
      }
      
      .contact-text {
        font-size: 18px;
        color: #333;
        font-weight: 500;
      }
    }
  }
}

// 联系表单区域
.contact-form-section {
  padding: 60px 0 80px;
  background: #f8f9fa;
  
  .form-header {
    margin-bottom: 40px;
    
    h2 {
      font-size: 28px;
      color: #0088cc;
      font-weight: 600;
      margin-bottom: 12px;
    }
    
    p {
      font-size: 15px;
      color: #666;
    }
  }
  
  .form-content {
    display: grid;
    grid-template-columns: 1fr 200px;
    gap: 40px;
    align-items: start;
  }
  
  .contact-form {
    background: white;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
    
    .form-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-bottom: 20px;
    }
    
    .form-group {
      margin-bottom: 20px;
      
      &.full-width {
        margin-bottom: 24px;
      }
      
      label {
        display: block;
        font-size: 14px;
        color: #333;
        margin-bottom: 8px;
        font-weight: 500;
        
        .required {
          color: #ff4d4f;
        }
      }
      
      input, textarea {
        width: 100%;
        padding: 12px 15px;
        border: 1px solid #e0e0e0;
        border-radius: 4px;
        font-size: 14px;
        transition: all 0.3s;
        box-sizing: border-box;
        background: #fff;
        
        &:focus {
          outline: none;
          border-color: #0088cc;
          box-shadow: 0 0 0 2px rgba(0, 136, 204, 0.1);
        }
        
        &::placeholder {
          color: #bbb;
        }
      }
      
      .phone-input {
        display: flex;
        align-items: center;
        border: 1px solid #e0e0e0;
        border-radius: 4px;
        overflow: hidden;
        background: #fff;
        
        &:focus-within {
          border-color: #0088cc;
          box-shadow: 0 0 0 2px rgba(0, 136, 204, 0.1);
        }
        
        .country-code {
          padding: 12px;
          background: #f9f9f9;
          border-right: 1px solid #e0e0e0;
          font-size: 16px;
        }
        
        input {
          border: none;
          
          &:focus {
            box-shadow: none;
          }
        }
      }
      
      textarea {
        resize: vertical;
        min-height: 120px;
      }
    }

    .submit-button {
      width: 100%;
      height: 48px;
      font-size: 16px;
      border-radius: 4px;
      cursor: pointer;
      background: #0088cc;
      color: white;
      border: none;
      font-weight: 500;
      transition: all 0.3s;
      
      &:hover {
        background: #0077b3;
      }
    }
  }
  
  .captcha-area {
    .captcha-box {
      width: 120px;
      height: 120px;
      background: #f0f0f0;
      border: 1px solid #ddd;
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      
      .captcha-text {
        font-size: 24px;
        color: #999;
        font-weight: 500;
      }
    }
  }
}

@media (max-width: 992px) {
  .company-intro .intro-grid {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  
  .contact-form-section .form-content {
    grid-template-columns: 1fr;
  }
  
  .contact-form-section .captcha-area {
    display: none;
  }
}

@media (max-width: 768px) {
  .page-header {
    height: 180px;
    
    .header-content {
      padding-left: 5%;
      
      h1 {
        font-size: 28px;
      }
      
      p {
        font-size: 14px;
      }
    }
    
    .header-bg-image::after {
      display: none;
    }
  }
  
  .contact-form-section .contact-form {
    padding: 24px;
    
    .form-row {
      grid-template-columns: 1fr;
      gap: 0;
    }
  }
}
</style>
