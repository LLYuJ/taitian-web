<template>
  <div class="contact-page">
    <!-- 页面头部 Banner（包含面包屑导航） -->
    <div class="page-header">
      <img 
        :src="headerBgImage" 
        alt="联系我们" 
        class="header-bg"
      />
      <div class="header-content">
        <nav class="breadcrumb">
          <router-link :to="localePath('/')">{{ t('nav.home') }}</router-link>
          <span class="separator">&gt;</span>
          <span class="current">{{ t('contactPage.title') }}</span>
        </nav>
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
import headerBg from '@/assets/images/backgrounds/page-header-bg.jpg'

const { t, localePath } = useLocale()

const companyImage = ref(companyImg)
const headerBgImage = ref(headerBg)

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
// 页面头部 Banner（包含面包屑导航）
.page-header {
  position: relative;
  height: 220px;
  display: flex;
  align-items: center;
  overflow: hidden;
  
  .header-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: 0;
  }
  
  .header-content {
    position: relative;
    z-index: 2;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    color: #333;
    
    .breadcrumb {
      display: flex;
      align-items: center;
      font-size: 14px;
      margin-bottom: 20px;
      
      a {
        color: #0066cc;
        text-decoration: none;
        
        &:hover {
          text-decoration: underline;
        }
      }
      
      .separator {
        margin: 0 8px;
        color: #666;
      }
      
      .current {
        color: #333;
      }
    }
    
    h1 {
      font-size: 36px;
      font-weight: 600;
      margin-bottom: 16px;
      letter-spacing: 1px;
      color: #333;
    }

    p {
      font-size: 16px;
      color: #666;
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
      padding: 0 15px;
      
      .breadcrumb {
        font-size: 12px;
        margin-bottom: 15px;
      }
      
      h1 {
        font-size: 24px;
      }
      
      p {
        font-size: 14px;
      }
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
