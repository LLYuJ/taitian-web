<template>
  <div class="about-page">
    <!-- 页面头部 Banner（包含面包屑导航） -->
    <div class="page-header">
      <img 
        :src="backgroundImage" 
        :alt="t('aboutPage.title')" 
        class="header-bg"
      />
      <div class="header-content">
        <nav class="breadcrumb">
          <router-link :to="localePath('/')">{{ t('nav.home') }}</router-link>
          <span class="separator">&gt;</span>
          <span class="current">{{ t('aboutPage.title') }}</span>
        </nav>
        <h1>{{ t('aboutPage.title') }}</h1>
        <p>{{ t('aboutPage.subtitle') }}</p>
      </div>
    </div>

    <section class="about-content">
      <div class="container">
        <div class="content-section">
          <h2>{{ t('aboutPage.companyInfo') }}</h2>
          <p>{{ t('aboutPage.companyDesc1') }}</p>
          <p>{{ t('aboutPage.companyDesc2') }}</p>
          <p>{{ t('aboutPage.companyDesc3') }}</p>
        </div>

        <div class="stats-section">
          <div class="stat-card" v-for="stat in stats" :key="stat.labelKey">
            <div class="stat-value">{{ stat.value }}</div>
            <div class="stat-unit">{{ t(stat.unitKey) }}</div>
            <div class="stat-label">{{ t(stat.labelKey) }}</div>
          </div>
        </div>

        <div class="content-section">
          <h2>{{ t('aboutPage.philosophy') }}</h2>
          <div class="philosophy-grid">
            <div class="philosophy-item card" v-for="item in philosophyItems" :key="item.titleKey">
              <div class="philosophy-icon" v-html="item.icon"></div>
              <h3>{{ t(item.titleKey) }}</h3>
              <p>{{ t(item.descKey) }}</p>
            </div>
          </div>
        </div>
        
        <div class="content-section">
          <h2>{{ t('aboutPage.rdStrength') }}</h2>
          <p>{{ t('aboutPage.rdDesc') }}</p>
          
          <div class="research-grid">
            <div class="research-item" v-for="item in researchItems" :key="item.titleKey">
              <img :src="item.image" :alt="t(item.titleKey)" loading="lazy" />
              <div class="research-info">
                <h4>{{ t(item.titleKey) }}</h4>
                <p>{{ t(item.descKey) }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useLocale } from '@/composables/useLocale'

import bgImage from '@/assets/images/backgrounds/page-header-bg.jpg'
import researchConcept from '@/assets/images/banners/research-concept.jpg'
import researchPractice from '@/assets/images/banners/research-practice.jpg'
import researchResource from '@/assets/images/banners/research-resource.jpg'

const { t, localePath } = useLocale()

const backgroundImage = ref(bgImage)

const stats = [
  { value: '2000', unitKey: 'aboutPage.stats.foundedUnit', labelKey: 'aboutPage.stats.founded' },
  { value: '6088', unitKey: 'aboutPage.stats.capitalUnit', labelKey: 'aboutPage.stats.capital' },
  { value: '1000', unitKey: 'aboutPage.stats.employeesUnit', labelKey: 'aboutPage.stats.employees' },
  { value: '3000', unitKey: 'aboutPage.stats.cncUnit', labelKey: 'aboutPage.stats.cnc' },
  { value: '120', unitKey: 'aboutPage.stats.patentsUnit', labelKey: 'aboutPage.stats.patents' }
]

// 专业 SVG 图标
const svgIcons = {
  innovation: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M9 18h6"/>
    <path d="M10 22h4"/>
    <path d="M12 2a7 7 0 0 0-4 12.9V17a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-2.1A7 7 0 0 0 12 2z"/>
    <path d="M12 6v4"/>
    <path d="M10 8h4"/>
  </svg>`,
  quality: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
  </svg>`,
  service: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
    <circle cx="9" cy="7" r="4"/>
    <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
    <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
  </svg>`,
  expertise: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="10"/>
    <circle cx="12" cy="12" r="6"/>
    <circle cx="12" cy="12" r="2"/>
  </svg>`
}

const philosophyItems = [
  { icon: svgIcons.innovation, titleKey: 'aboutPage.philosophyItems.innovation', descKey: 'aboutPage.philosophyItems.innovationDesc' },
  { icon: svgIcons.quality, titleKey: 'aboutPage.philosophyItems.quality', descKey: 'aboutPage.philosophyItems.qualityDesc' },
  { icon: svgIcons.service, titleKey: 'aboutPage.philosophyItems.service', descKey: 'aboutPage.philosophyItems.serviceDesc' },
  { icon: svgIcons.expertise, titleKey: 'aboutPage.philosophyItems.expertise', descKey: 'aboutPage.philosophyItems.expertiseDesc' }
]

const researchItems = [
  { titleKey: 'aboutPage.rdConcept', descKey: 'aboutPage.rdConceptDesc', image: researchConcept },
  { titleKey: 'aboutPage.rdPractice', descKey: 'aboutPage.rdPracticeDesc', image: researchPractice },
  { titleKey: 'aboutPage.rdResource', descKey: 'aboutPage.rdResourceDesc', image: researchResource }
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

.about-content {
  padding: 80px 0;

  .content-section {
    margin-bottom: 60px;

    h2 {
      font-size: 32px;
      color: #333;
      margin-bottom: 30px;
      position: relative;
      padding-left: 20px;

      &::before {
        content: '';
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 4px;
        height: 32px;
        background: #2CB5BE;
      }
    }

    p {
      font-size: 16px;
      line-height: 1.9;
      color: #666;
      margin-bottom: 20px;
    }
  }
  
  .stats-section {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 20px;
    margin: 60px 0;
    
    .stat-card {
      background: linear-gradient(135deg, #2CB5BE 0%, #1a8a91 100%);
      border-radius: 12px;
      padding: 30px 20px;
      text-align: center;
      color: white;
      transition: all 0.3s;
      
      &:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(44, 181, 190, 0.4);
      }
      
      .stat-value {
        font-size: 36px;
        font-weight: 700;
      }
      
      .stat-unit {
        font-size: 18px;
        opacity: 0.9;
        margin-bottom: 10px;
      }
      
      .stat-label {
        font-size: 14px;
        opacity: 0.8;
      }
    }
  }

  .philosophy-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 25px;
    margin-top: 40px;
  }

  .philosophy-item {
    padding: 35px 25px;
    text-align: center;
    background: #f8f9fa;
    border-radius: 12px;
    transition: all 0.3s;
    
    &:hover {
      background: white;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
      
      .philosophy-icon {
        background: #2CB5BE;
        color: white;
        transform: scale(1.05);
      }
    }
    
    .philosophy-icon {
      width: 72px;
      height: 72px;
      margin: 0 auto 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, #e8f7f8 0%, #d0f0f3 100%);
      border-radius: 16px;
      color: #2CB5BE;
      transition: all 0.3s ease;
      
      :deep(svg) {
        width: 36px;
        height: 36px;
      }
    }

    h3 {
      font-size: 20px;
      color: #2CB5BE;
      margin-bottom: 12px;
    }

    p {
      font-size: 14px;
      color: #666;
      line-height: 1.6;
      margin: 0;
    }
  }
  
  .research-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    margin-top: 40px;
    
    .research-item {
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
      transition: all 0.3s;
      
      &:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
      }
      
      img {
        width: 100%;
        height: 180px;
        object-fit: cover;
      }
      
      .research-info {
        padding: 20px;
        background: white;
        text-align: center;
        
        h4 {
          font-size: 18px;
          color: #2CB5BE;
          margin-bottom: 8px;
        }
        
        p {
          font-size: 14px;
          color: #666;
          margin: 0;
        }
      }
    }
  }
}

@media (max-width: 992px) {
  .about-content {
    .stats-section {
      grid-template-columns: repeat(3, 1fr);
    }
    
    .philosophy-grid {
      grid-template-columns: repeat(2, 1fr);
    }
    
    .research-grid {
      grid-template-columns: repeat(2, 1fr);
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
  
  .about-content {
    .stats-section {
      grid-template-columns: repeat(2, 1fr);
    }
    
    .philosophy-grid,
    .research-grid {
      grid-template-columns: 1fr;
    }
  }
}
</style>
