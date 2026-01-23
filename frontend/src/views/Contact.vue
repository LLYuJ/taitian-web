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
              <span class="contact-icon-svg">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/>
                </svg>
              </span>
              <span class="contact-text">400-826-1128</span>
            </div>
            <div class="contact-item">
              <span class="contact-icon-svg">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
                </svg>
              </span>
              <span class="contact-text">sales@chinataitian.com</span>
            </div>
            <div class="contact-item">
              <span class="contact-icon-svg">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
                </svg>
              </span>
              <span class="contact-text">{{ t('contactPage.addressValue') }}</span>
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
                  <div class="phone-input-group">
                    <span class="plus-sign">+</span>
                    <input 
                      v-model="form.areaCode" 
                      type="text" 
                      class="area-code-input"
                      :placeholder="t('contactPage.form.areaCodePlaceholder')"
                    />
                    <input 
                      v-model="form.phone" 
                      type="tel" 
                      class="phone-number-input"
                      :placeholder="t('contactPage.form.phonePlaceholder')"
                    />
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
          
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useLocale } from '@/composables/useLocale'

import companyImg from '@/assets/images/banners/new_door.png'
import headerBg from '@/assets/images/backgrounds/page-header-bg.jpg'

const { t, localePath } = useLocale()

const companyImage = ref(companyImg)
const headerBgImage = ref(headerBg)

const form = reactive({
  name: '',
  company: '',
  areaCode: '',
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
  form.areaCode = ''
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
      margin-bottom: 16px;
      
      &:last-child {
        margin-bottom: 0;
      }
      
      .contact-icon {
        width: 24px;
        height: 24px;
        object-fit: contain;
      }
      
      .contact-icon-svg {
        width: 24px;
        height: 24px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #0088cc;
        flex-shrink: 0;
        
        svg {
          width: 20px;
          height: 20px;
        }
      }
      
      .contact-text {
        font-size: 16px;
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
    display: block;
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
      
      textarea {
        resize: vertical;
        min-height: 120px;
      }
      
      .phone-input-group {
        display: flex;
        align-items: center;
        border: 1px solid #e0e0e0;
        border-radius: 4px;
        overflow: hidden;
        background: #fff;
        transition: all 0.3s;
        
        &:focus-within {
          border-color: #0088cc;
          box-shadow: 0 0 0 2px rgba(0, 136, 204, 0.1);
        }
        
        .plus-sign {
          padding: 12px 8px 12px 15px;
          color: #666;
          font-size: 14px;
          font-weight: 500;
          background: #f9f9f9;
          user-select: none;
        }
        
        .area-code-input {
          width: 60px;
          min-width: 60px;
          padding: 12px 8px;
          border: none;
          border-right: 1px solid #e0e0e0;
          background: #f9f9f9;
          text-align: center;
          font-size: 14px;
          
          &:focus {
            outline: none;
            box-shadow: none;
          }
          
          &::placeholder {
            color: #bbb;
          }
        }
        
        .phone-number-input {
          flex: 1;
          padding: 12px 15px;
          border: none;
          font-size: 14px;
          
          &:focus {
            outline: none;
            box-shadow: none;
          }
          
          &::placeholder {
            color: #bbb;
          }
        }
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
  
}

@media (max-width: 992px) {
  .company-intro .intro-grid {
    grid-template-columns: 1fr;
    gap: 40px;
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
