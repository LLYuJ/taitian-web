<template>
  <div class="services-page">
    <!-- 页面头部 Banner（包含面包屑导航） -->
    <div class="page-header">
      <img 
        :src="headerBg" 
        :alt="pageTitle" 
        class="header-bg"
      />
      <div class="header-content">
        <nav class="breadcrumb">
          <router-link :to="localePath('/')">{{ t('nav.home') }}</router-link>
          <span class="separator">&gt;</span>
          <template v-if="isSubPage">
            <router-link :to="localePath('/services')">{{ t('nav.services') }}</router-link>
            <span class="separator">&gt;</span>
            <span class="current">{{ currentTabLabel }}</span>
          </template>
          <template v-else>
            <span class="current">{{ t('nav.services') }}</span>
          </template>
        </nav>
        <h1>{{ pageTitle }}</h1>
        <p>{{ pageSubtitle }}</p>
      </div>
    </div>

    <!-- 分类标签：售前资讯 / 售后保障 / 产品资料 -->
    <section class="category-tabs">
      <div class="container">
        <div class="tabs">
          <router-link 
            :to="localePath('/services')" 
            class="tab-item"
            :class="{ active: currentTab === 'pre-sales' && !isSubPage }"
          >
            {{ t('servicesPage.preSales.tabName') }}
          </router-link>
          <router-link 
            :to="localePath('/services/after-sales')" 
            class="tab-item"
            :class="{ active: currentTab === 'after-sales' }"
          >
            {{ t('servicesPage.afterSales.tabName') }}
          </router-link>
          <router-link 
            :to="localePath('/services/documents')" 
            class="tab-item"
            :class="{ active: currentTab === 'documents' }"
          >
            {{ t('servicesPage.documents.tabName') }}
          </router-link>
        </div>
      </div>
    </section>

    <!-- 内容区域 -->
    <section class="services-content">
      <div class="container">
        <!-- 售前资讯内容 -->
        <template v-if="currentTab === 'pre-sales'">
          <!-- 服务流程 -->
          <div class="process-section">
            <div class="process-flow">
              <div class="process-step" v-for="(step, index) in processSteps" :key="index">
                <div class="step-icon">
                  <span class="step-number">{{ index + 1 }}</span>
                </div>
                <div class="step-label">{{ step }}</div>
                <div class="step-arrow" v-if="index < processSteps.length - 1">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path d="M9 6L15 12L9 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
              </div>
            </div>
          </div>

          <!-- 常见Q&A -->
          <div class="faq-section">
            <h2 class="section-title">{{ t('servicesPage.preSales.faqTitle') }}</h2>
            <div class="faq-list">
              <div 
                class="faq-item" 
                v-for="(faq, index) in faqList" 
                :key="index"
                :class="{ expanded: expandedFaq === index }"
              >
                <div class="faq-question" @click="toggleFaq(index)">
                  <span class="question-text">{{ faq.question }}</span>
                  <span class="toggle-icon">
                    <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                      <path 
                        :d="expandedFaq === index ? 'M5 12L10 7L15 12' : 'M5 8L10 13L15 8'" 
                        stroke="currentColor" 
                        stroke-width="2" 
                        stroke-linecap="round" 
                        stroke-linejoin="round"
                      />
                    </svg>
                  </span>
                </div>
                <div class="faq-answer" v-show="expandedFaq === index">
                  <p>{{ faq.answer }}</p>
                </div>
              </div>
            </div>
          </div>
        </template>

        <!-- 售后保障内容 -->
        <template v-else-if="currentTab === 'after-sales'">
          <div class="maintenance-section">
            <!-- 维修与保养服务标题 -->
            <h2 class="section-title">{{ t('servicesPage.afterSales.maintenanceTitle') }}</h2>
            
            <!-- 三个维修保养卡片 -->
            <div class="maintenance-cards">
              <!-- 压缩机维修与保养 -->
              <div class="maintenance-card">
                <h3 class="card-title">{{ t('servicesPage.afterSales.compressor.title') }}</h3>
                <div class="card-divider"></div>
                <div class="card-items">
                  <span 
                    v-for="(item, index) in compressorItems" 
                    :key="index"
                    class="item-tag"
                  >{{ item }}</span>
                </div>
              </div>
              
              <!-- 主机维修与保养 -->
              <div class="maintenance-card">
                <h3 class="card-title">{{ t('servicesPage.afterSales.host.title') }}</h3>
                <div class="card-divider"></div>
                <div class="card-items">
                  <span 
                    v-for="(item, index) in hostItems" 
                    :key="index"
                    class="item-tag"
                  >{{ item }}</span>
                </div>
              </div>
              
              <!-- 工具维修与保养 -->
              <div class="maintenance-card">
                <h3 class="card-title">{{ t('servicesPage.afterSales.tools.title') }}</h3>
                <div class="card-divider"></div>
                <div class="card-items">
                  <span 
                    v-for="(item, index) in toolItems" 
                    :key="index"
                    class="item-tag"
                  >{{ item }}</span>
                </div>
              </div>
            </div>
          </div>
        </template>

        <!-- 产品资料内容 -->
        <template v-else-if="currentTab === 'documents'">
          <div class="content-placeholder">
            <!-- 预留内容区域 -->
          </div>
        </template>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useLocale } from '@/composables/useLocale'

import bgImage from '@/assets/images/backgrounds/page-header-bg.jpg'

const { t, tm, localePath } = useLocale()
const route = useRoute()

const headerBg = ref(bgImage)
const expandedFaq = ref(0) // 默认展开第一个

// 判断当前标签
const currentTab = computed(() => {
  const path = route.path
  if (path.includes('/services/after-sales')) return 'after-sales'
  if (path.includes('/services/documents')) return 'documents'
  return 'pre-sales' // 默认售前资讯
})

// 判断是否为子页面（有明确的子路由）
const isSubPage = computed(() => {
  const path = route.path
  return path.includes('/services/after-sales') || path.includes('/services/documents')
})

// 当前标签的显示名称
const currentTabLabel = computed(() => {
  switch (currentTab.value) {
    case 'after-sales':
      return t('servicesPage.afterSales.tabName')
    case 'documents':
      return t('servicesPage.documents.tabName')
    default:
      return t('servicesPage.preSales.tabName')
  }
})

// 页面标题（根据当前标签变化）
const pageTitle = computed(() => {
  switch (currentTab.value) {
    case 'after-sales':
      return t('servicesPage.afterSales.title')
    case 'documents':
      return t('servicesPage.documents.title')
    default:
      return t('servicesPage.preSales.title')
  }
})

// 页面副标题（根据当前标签变化）
const pageSubtitle = computed(() => {
  switch (currentTab.value) {
    case 'after-sales':
      return t('servicesPage.afterSales.desc')
    case 'documents':
      return t('servicesPage.documents.desc')
    default:
      return t('servicesPage.preSales.desc')
  }
})

// 服务流程步骤
const processSteps = computed(() => [
  t('servicesPage.preSales.process.step1'),
  t('servicesPage.preSales.process.step2'),
  t('servicesPage.preSales.process.step3'),
  t('servicesPage.preSales.process.step4'),
  t('servicesPage.preSales.process.step5')
])

// 售后维修保养数据
const compressorItems = computed(() => tm('servicesPage.afterSales.compressor.items'))
const hostItems = computed(() => tm('servicesPage.afterSales.host.items'))
const toolItems = computed(() => tm('servicesPage.afterSales.tools.items'))

// FAQ 列表
const faqList = computed(() => [
  {
    question: t('servicesPage.preSales.faq.q1'),
    answer: t('servicesPage.preSales.faq.a1')
  },
  {
    question: t('servicesPage.preSales.faq.q2'),
    answer: t('servicesPage.preSales.faq.a2')
  },
  {
    question: t('servicesPage.preSales.faq.q3'),
    answer: t('servicesPage.preSales.faq.a3')
  },
  {
    question: t('servicesPage.preSales.faq.q4'),
    answer: t('servicesPage.preSales.faq.a4')
  },
  {
    question: t('servicesPage.preSales.faq.q5'),
    answer: t('servicesPage.preSales.faq.a5')
  },
  {
    question: t('servicesPage.preSales.faq.q6'),
    answer: t('servicesPage.preSales.faq.a6')
  }
])

// 切换 FAQ 展开状态
const toggleFaq = (index) => {
  expandedFaq.value = expandedFaq.value === index ? -1 : index
}
</script>

<style lang="scss" scoped>
$primary-color: #2CB5BE;
$primary-light: #e8f7f8;
$primary-dark: #239aa2;

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

.category-tabs {
  background: #fff;
  padding: 20px 0;
  
  .tabs {
    display: flex;
    gap: 16px;
    
    .tab-item {
      padding: 10px 28px;
      color: #666;
      text-decoration: none;
      font-size: 14px;
      border: 1px solid #ddd;
      border-radius: 50px;
      background: #fff;
      transition: all 0.3s;
      
      &:hover {
        border-color: $primary-color;
        color: $primary-color;
      }
      
      &.active {
        background: $primary-color;
        border-color: $primary-color;
        color: #fff;
      }
    }
  }
}

.services-content {
  padding: 50px 0;
  background: #fff;
  min-height: 400px;

  .content-placeholder {
    min-height: 300px;
  }
}

// 售后维修保养样式
.maintenance-section {
  .section-title {
    font-size: 28px;
    font-weight: 600;
    color: #333;
    margin-bottom: 48px;
    text-align: center;
    position: relative;
    
    &::after {
      content: '';
      display: block;
      width: 60px;
      height: 3px;
      background: $primary-color;
      margin: 16px auto 0;
      border-radius: 2px;
    }
  }
  
  .maintenance-cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
    max-width: 1100px;
    margin: 0 auto;
  }
  
  .maintenance-card {
    background: #fff;
    border-radius: 12px;
    padding: 32px 28px;
    border: 1px solid #e8e8e8;
    transition: all 0.3s ease;
    
    &:hover {
      border-color: rgba($primary-color, 0.5);
      box-shadow: 0 8px 24px rgba($primary-color, 0.1);
      transform: translateY(-4px);
    }
    
    .card-title {
      font-size: 18px;
      font-weight: 600;
      color: #333;
      margin: 0 0 16px 0;
    }
    
    .card-divider {
      height: 2px;
      background: linear-gradient(90deg, $primary-color 0%, rgba($primary-color, 0.3) 100%);
      margin-bottom: 24px;
      border-radius: 1px;
    }
    
    .card-items {
      display: flex;
      flex-wrap: wrap;
      gap: 12px 24px;
    }
    
    .item-tag {
      font-size: 15px;
      color: #555;
      position: relative;
      
      &::before {
        content: '';
        display: inline-block;
        width: 4px;
        height: 4px;
        background: $primary-color;
        border-radius: 50%;
        margin-right: 8px;
        vertical-align: middle;
      }
    }
  }
}

@media (max-width: 900px) {
  .maintenance-section {
    .maintenance-cards {
      grid-template-columns: 1fr;
      gap: 24px;
    }
    
    .section-title {
      font-size: 24px;
      margin-bottom: 32px;
    }
  }
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

// 服务流程样式
.process-section {
  margin-bottom: 60px;
  
  .process-flow {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 40px 20px;
    background: linear-gradient(135deg, $primary-light 0%, #fff 100%);
    border-radius: 16px;
    border: 1px solid rgba($primary-color, 0.2);
  }
  
  .process-step {
    display: flex;
    align-items: center;
    
    .step-icon {
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: linear-gradient(135deg, $primary-color 0%, $primary-dark 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 12px rgba($primary-color, 0.3);
      
      .step-number {
        color: #fff;
        font-size: 20px;
        font-weight: 600;
      }
    }
    
    .step-label {
      margin-left: 12px;
      font-size: 15px;
      font-weight: 500;
      color: #333;
      white-space: nowrap;
    }
    
    .step-arrow {
      margin: 0 20px;
      color: $primary-color;
      display: flex;
      align-items: center;
      
      svg {
        width: 28px;
        height: 28px;
      }
    }
  }
}

// FAQ 样式
.faq-section {
  .section-title {
    font-size: 28px;
    font-weight: 600;
    color: #333;
    margin-bottom: 32px;
    text-align: center;
    position: relative;
    
    &::after {
      content: '';
      display: block;
      width: 60px;
      height: 3px;
      background: $primary-color;
      margin: 16px auto 0;
      border-radius: 2px;
    }
  }
  
  .faq-list {
    max-width: 900px;
    margin: 0 auto;
  }
  
  .faq-item {
    border: 1px solid #e8e8e8;
    border-radius: 12px;
    margin-bottom: 16px;
    overflow: hidden;
    transition: all 0.3s ease;
    
    &:hover {
      border-color: rgba($primary-color, 0.5);
    }
    
    &.expanded {
      border-color: $primary-color;
      box-shadow: 0 4px 16px rgba($primary-color, 0.15);
      
      .faq-question {
        background: $primary-light;
        color: $primary-dark;
      }
      
      .toggle-icon {
        color: $primary-color;
      }
    }
    
    .faq-question {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 20px 24px;
      cursor: pointer;
      background: #fafafa;
      transition: all 0.3s ease;
      
      &:hover {
        background: $primary-light;
      }
      
      .question-text {
        font-size: 16px;
        font-weight: 500;
        color: #333;
        flex: 1;
        padding-right: 16px;
      }
      
      .toggle-icon {
        color: #999;
        transition: color 0.3s;
        flex-shrink: 0;
      }
    }
    
    .faq-answer {
      padding: 20px 24px;
      background: #fff;
      border-top: 1px solid #e8e8e8;
      
      p {
        font-size: 15px;
        line-height: 1.8;
        color: #666;
        margin: 0;
      }
    }
  }
}

@media (max-width: 1024px) {
  .process-section {
    .process-flow {
      flex-wrap: wrap;
      gap: 20px;
      padding: 30px 20px;
    }
    
    .process-step {
      .step-arrow {
        display: none;
      }
      
      .step-icon {
        width: 48px;
        height: 48px;
        
        .step-number {
          font-size: 18px;
        }
      }
      
      .step-label {
        font-size: 14px;
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
  
  .category-tabs .tabs {
    gap: 10px;
    flex-wrap: wrap;
    
    .tab-item {
      padding: 8px 18px;
      font-size: 13px;
    }
  }
  
  .process-section {
    margin-bottom: 40px;
    
    .process-flow {
      flex-direction: column;
      align-items: stretch;
      gap: 12px;
      padding: 24px 16px;
    }
    
    .process-step {
      justify-content: flex-start;
      padding: 12px 16px;
      background: #fff;
      border-radius: 8px;
      
      .step-icon {
        width: 40px;
        height: 40px;
        
        .step-number {
          font-size: 16px;
        }
      }
      
      .step-label {
        font-size: 14px;
      }
    }
  }
  
  .faq-section {
    .section-title {
      font-size: 22px;
      margin-bottom: 24px;
    }
    
    .faq-item {
      .faq-question {
        padding: 16px;
        
        .question-text {
          font-size: 14px;
        }
      }
      
      .faq-answer {
        padding: 16px;
        
        p {
          font-size: 14px;
        }
      }
    }
  }
}
</style>
