<template>
  <div class="applications-page">
    <!-- 页面头部 Banner（包含面包屑导航） -->
    <div class="page-header">
      <img 
        :src="headerBgImage" 
        alt="应用领域" 
        class="header-bg"
      />
      <div class="header-content">
        <nav class="breadcrumb">
          <router-link :to="localePath('/')">{{ t('nav.home') }}</router-link>
          <span class="separator">&gt;</span>
          <span class="current">{{ t('applicationsPage.title') }}</span>
        </nav>
        <h1>{{ t('applicationsPage.title') }}</h1>
        <p>{{ t('applicationsPage.subtitle') }}</p>
      </div>
    </div>

    <section class="applications-content">
      <div class="container">
        <div class="applications-grid">
          <div class="application-card card" v-for="app in applications" :key="app.titleKey">
            <div class="card-icon" v-html="app.icon"></div>
            <h3>{{ t(app.titleKey) }}</h3>
            <p>{{ t(app.descKey) }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useLocale } from '@/composables/useLocale'

import headerBg from '@/assets/images/backgrounds/page-header-bg.jpg'

const { t, localePath } = useLocale()

const headerBgImage = ref(headerBg)

// 专业 SVG 图标
const svgIcons = {
  automotive: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M5 17a2 2 0 1 0 4 0 2 2 0 0 0-4 0zm10 0a2 2 0 1 0 4 0 2 2 0 0 0-4 0z"/>
    <path d="M3 17h2m10 0h6V6a1 1 0 0 0-1-1h-6l-2 4H4a1 1 0 0 0-1 1v7zm2-5h6"/>
    <path d="M7 10l1.5-3h7"/>
  </svg>`,
  precision: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="3"/>
    <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/>
  </svg>`,
  automation: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <rect x="3" y="11" width="4" height="10" rx="1"/>
    <rect x="17" y="11" width="4" height="10" rx="1"/>
    <path d="M7 15h10"/>
    <path d="M12 15V7"/>
    <circle cx="12" cy="4" r="2"/>
    <path d="M9 6l3 1 3-1"/>
  </svg>`,
  repair: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
  </svg>`,
  fluid: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/>
  </svg>`
}

const applications = [
  { 
    icon: svgIcons.automotive, 
    titleKey: 'applicationsPage.automotive', 
    descKey: 'applicationsPage.automotiveDesc' 
  },
  { 
    icon: svgIcons.precision, 
    titleKey: 'applicationsPage.precision', 
    descKey: 'applicationsPage.precisionDesc' 
  },
  { 
    icon: svgIcons.automation, 
    titleKey: 'applicationsPage.automation', 
    descKey: 'applicationsPage.automationDesc' 
  },
  { 
    icon: svgIcons.repair, 
    titleKey: 'applicationsPage.repair', 
    descKey: 'applicationsPage.repairDesc' 
  },
  { 
    icon: svgIcons.fluid, 
    titleKey: 'applicationsPage.fluid', 
    descKey: 'applicationsPage.fluidDesc' 
  }
]
</script>

<style lang="scss" scoped>
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
        color: #000000;
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

.applications-content {
  padding: 80px 0;
  background: white;

  .applications-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
  }

  .application-card {
    padding: 45px 30px;
    text-align: center;

    .card-icon {
      width: 88px;
      height: 88px;
      margin: 0 auto 25px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, #e8f7f8 0%, #d0f0f3 100%);
      border-radius: 20px;
      color: #2CB5BE;
      transition: all 0.3s ease;
      
      :deep(svg) {
        width: 44px;
        height: 44px;
      }
    }

    h3 {
      font-size: 22px;
      color: #333;
      margin-bottom: 15px;
    }

    p {
      font-size: 15px;
      color: #666;
      line-height: 1.8;
      margin: 0;
    }

    &:hover {
      .card-icon {
        background: #2CB5BE;
        color: white;
        transform: scale(1.08) rotate(-3deg);
        box-shadow: 0 8px 25px rgba(44, 181, 190, 0.35);
      }
    }
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
  
  .applications-content .applications-grid {
    grid-template-columns: 1fr;
  }
}
</style>
