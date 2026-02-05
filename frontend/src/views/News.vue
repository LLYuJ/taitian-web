<template>
  <div class="news-page">
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
            <router-link :to="localePath('/news')">{{ t('newsPage.title') }}</router-link>
            <span class="separator">&gt;</span>
            <span class="current">{{ pageTitle }}</span>
          </template>
          <template v-else>
            <span class="current">{{ t('newsPage.bannerTitle') }}</span>
          </template>
        </nav>
        <h1>{{ pageTitle }}</h1>
        <p>{{ pageSubtitle }}</p>
      </div>
    </div>

    <!-- 分类标签：全部 / 泰田新闻 / 展会现场（始终显示，非预览时） -->
    <section v-if="!isPreviewMode" class="category-tabs">
      <div class="container">
        <div class="tabs">
          <router-link 
            :to="localePath('/news')" 
            class="tab-item"
            :class="{ active: !currentCategory }"
          >
            全部
          </router-link>
          <router-link 
            :to="localePath('/news/company')" 
            class="tab-item"
            :class="{ active: currentCategory === 'company' }"
          >
            泰田新闻
          </router-link>
          <router-link 
            :to="localePath('/news/exhibitions')" 
            class="tab-item"
            :class="{ active: currentCategory === 'exhibition' }"
          >
            展会现场
          </router-link>
        </div>
      </div>
    </section>

    <!-- 预览模式提示 -->
    <div v-if="isPreviewMode" class="preview-banner">
      <div class="container">
        <span class="preview-icon">👁</span>
        <span>预览模式 - 此内容尚未发布</span>
      </div>
    </div>

    <section class="news-content">
      <div class="container">
        <!-- 加载状态 -->
        <div v-if="loading" class="loading-state">
          <div class="loading-spinner"></div>
          <p>{{ t('common.loading') }}</p>
        </div>

        <!-- 新闻列表 -->
        <div v-else class="news-list">
          <router-link 
            class="news-item" 
            v-for="item in newsList" 
            :key="item.id"
            :to="localePath(`/news/detail/${item.id}`)"
          >
            <div class="news-image">
              <img :src="item.image_url || defaultImage" :alt="item.title" loading="lazy" />
            </div>
            <div class="news-info">
              <h3>{{ item.title }}</h3>
              <span class="news-date">{{ formatDate(item.published_at || item.created_at) }}</span>
              <p>{{ item.summary }}</p>
            </div>
          </router-link>

          <!-- 空状态 -->
          <div v-if="newsList.length === 0" class="empty-state">
            <p>暂无新闻资讯</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useLocale } from '@/composables/useLocale'
import axios from '@/utils/axios'

import bgImage from '@/assets/images/backgrounds/page-header-bg.jpg'
import news1 from '@/assets/images/news/news1.jpg'

const { t, localePath } = useLocale()
const route = useRoute()

const headerBg = ref(bgImage)
const defaultImage = news1
const loading = ref(false)
const newsList = ref([])

// 判断是否为预览模式
const isPreviewMode = computed(() => {
  return !!route.query.token
})

// 判断当前分类
const currentCategory = computed(() => {
  const path = route.path
  if (path.includes('/news/company')) return 'company'
  if (path.includes('/news/exhibitions')) return 'exhibition'
  return null
})

// 判断是否为子页面
const isSubPage = computed(() => {
  return currentCategory.value !== null || isPreviewMode.value
})

// 页面标题（主页面用「新闻与资讯」，子页面用分类名）
const pageTitle = computed(() => {
  if (isPreviewMode.value) {
    return newsList.value[0]?.title || t('newsPage.title')
  }
  if (currentCategory.value === 'company') {
    return t('nav.sub.companyNews')
  }
  if (currentCategory.value === 'exhibition') {
    return t('nav.sub.exhibitions')
  }
  return t('newsPage.bannerTitle')
})

// 页面副标题（主页面用指定文案，子页面用分类描述）
const pageSubtitle = computed(() => {
  if (currentCategory.value === 'company') {
    return t('newsPage.companyNews.desc')
  }
  if (currentCategory.value === 'exhibition') {
    return t('newsPage.exhibitions.desc')
  }
  return t('newsPage.bannerSubtitle')
})

// 格式化日期
const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  })
}

// 加载新闻列表
const loadNews = async () => {
  loading.value = true
  try {
    // 预览模式
    if (isPreviewMode.value) {
      const token = route.query.token
      const response = await axios.get(`/api/v1/news/preview/${token}`)
      newsList.value = [response.data]
      return
    }

    // 正常模式
    const params = {}
    if (currentCategory.value) {
      params.category = currentCategory.value
    }
    
    const response = await axios.get('/api/v1/news/list', { params })
    newsList.value = response.data
  } catch (error) {
    console.error('加载新闻失败:', error)
    // 如果 API 失败，显示静态数据
    newsList.value = getStaticNews()
  } finally {
    loading.value = false
  }
}

// 静态新闻数据（API 不可用时的备用）
const getStaticNews = () => {
  const allNews = [
    {
      id: 1,
      title: '2019年上海国际工业装配与传输技术展览会',
      summary: '2019年上海国际工业装配与传输技术展览会，将于2019年7月在上海举行。泰田集团将携旗下核心产品亮相展会，展示公司在工业装配领域的最新技术成果和解决方案。',
      published_at: '2020-04-11',
      image_url: null,
      category: 'exhibition'
    },
    {
      id: 2,
      title: '泰田集团喜获"浙江名牌产品"称号',
      summary: '"浙江名牌"荣誉是经区、市级质量监督管理部门严格审核通过，由浙江省质量技术监督局认定授予的称号。泰田集团凭借卓越的产品质量和良好的市场口碑荣获此殊荣。',
      published_at: '2018-10-29',
      image_url: null,
      category: 'company'
    },
    {
      id: 3,
      title: '《冲击式气扳机》"浙江制造"团体标准评审会在我司召开',
      summary: '"浙江制造"是浙江省启动的将"浙江制造"打造成为具有严格认证要求的区域公共品牌的重要举措。本次评审会的召开标志着泰田集团在行业标准制定方面迈出重要一步。',
      published_at: '2020-04-11',
      image_url: null,
      category: 'company'
    },
    {
      id: 4,
      title: '泰田集团通过浙江省省级企业研究院认定',
      summary: '省科技厅近日公布了2018年省级企业研究院认定名单，泰田集团榜上有名。这标志着公司的研发创新能力得到了省级认可，将进一步推动公司技术创新和产品升级。',
      published_at: '2018-10-19',
      image_url: null,
      category: 'company'
    },
    {
      id: 5,
      title: '泰田集团参加2018年秋季校园招聘会',
      summary: '"问渠哪得清如许，为有源头活水来"，一个公司要发展壮大、团队要永葆活力，就需要不断注入新鲜血液。泰田集团积极参与校园招聘，为公司发展储备优秀人才。',
      published_at: '2020-04-11',
      image_url: null,
      category: 'company'
    }
  ]

  if (currentCategory.value) {
    return allNews.filter(n => n.category === currentCategory.value)
  }
  return allNews
}

// 监听路由变化重新加载
watch(() => route.path, () => {
  loadNews()
})

watch(() => route.query.token, () => {
  loadNews()
})

onMounted(() => {
  loadNews()
})
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
        border-color: #2CB5BE;
        color: #2CB5BE;
      }
      
      &.active {
        background: #2CB5BE;
        border-color: #2CB5BE;
        color: #fff;
      }
    }
  }
}

.preview-banner {
  background: #fff3cd;
  padding: 12px 0;
  
  .container {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #856404;
    font-size: 14px;
  }
  
  .preview-icon {
    font-size: 18px;
  }
}

.news-content {
  padding: 50px 0;
  background: #fff;

  .loading-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 300px;
    
    .loading-spinner {
      width: 40px;
      height: 40px;
      border: 3px solid #eee;
      border-top-color: #2CB5BE;
      border-radius: 50%;
      animation: spin 1s linear infinite;
    }
    
    p {
      margin-top: 16px;
      color: #666;
    }
  }

  .news-list {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
  }

  .news-item {
    display: block;
    text-decoration: none;
    color: inherit;
    
    &:hover {
      .news-image img {
        transform: scale(1.05);
      }
      
      h3 {
        color: #2CB5BE;
      }
    }

    .news-image {
      width: 100%;
      height: 180px;
      overflow: hidden;
      margin-bottom: 16px;
      
      img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.4s;
      }
    }

    .news-info {
      h3 {
        font-size: 16px;
        font-weight: 600;
        color: #333;
        margin-bottom: 8px;
        line-height: 1.5;
        transition: color 0.3s;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
      }

      .news-date {
        display: block;
        font-size: 13px;
        color: #999;
        margin-bottom: 12px;
      }

      p {
        font-size: 14px;
        color: #666;
        line-height: 1.8;
        display: -webkit-box;
        -webkit-line-clamp: 5;
        -webkit-box-orient: vertical;
        overflow: hidden;
      }
    }
  }

  .empty-state {
    grid-column: 1 / -1;
    text-align: center;
    padding: 80px 20px;
    color: #999;
    
    p {
      font-size: 16px;
    }
  }
}

@keyframes spin {
  to {
    transform: rotate(360deg);
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
    
    .tab-item {
      padding: 8px 18px;
      font-size: 13px;
    }
  }
  
  .news-content .news-list {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 1024px) {
  .news-content .news-list {
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
  }
}
</style>
