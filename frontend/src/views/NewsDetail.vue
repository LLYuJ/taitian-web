<template>
  <div class="news-detail-page">
    <!-- 页面头部 Banner -->
    <div class="page-header">
      <img 
        :src="headerBg" 
        :alt="t('newsPage.title')" 
        class="header-bg"
      />
      <div class="header-content">
        <nav class="breadcrumb">
          <router-link :to="localePath('/')">{{ t('nav.home') }}</router-link>
          <span class="separator">&gt;</span>
          <router-link :to="localePath('/news')">{{ t('newsPage.title') }}</router-link>
          <span class="separator">&gt;</span>
          <span class="current">{{ news?.title || '新闻详情' }}</span>
        </nav>
        <h1>{{ t('newsPage.title') }}</h1>
      </div>
    </div>

    <!-- 预览模式提示 -->
    <div v-if="isPreviewMode" class="preview-banner">
      <div class="container">
        <span class="preview-icon">👁</span>
        <span>预览模式 - 此内容尚未发布</span>
      </div>
    </div>

    <section class="detail-content">
      <div class="container">
        <!-- 加载状态 -->
        <div v-if="loading" class="loading-state">
          <div class="loading-spinner"></div>
          <p>{{ t('common.loading') }}</p>
        </div>

        <!-- 错误状态 -->
        <div v-else-if="error" class="error-state">
          <p>{{ error }}</p>
          <router-link :to="localePath('/news')" class="back-link">
            ← 返回新闻列表
          </router-link>
        </div>

        <!-- 新闻详情 -->
        <article v-else-if="news" class="news-article">
          <!-- 文章头部 -->
          <header class="article-header">
            <div class="article-meta">
              <span class="category-tag" :class="news.category">
                {{ news.category === 'company' ? t('nav.sub.companyNews') : t('nav.sub.exhibitions') }}
              </span>
              <span class="publish-date">
                {{ formatDate(news.published_at || news.created_at) }}
              </span>
            </div>
            <h1 class="article-title">{{ news.title }}</h1>
            <p v-if="news.summary" class="article-summary">{{ news.summary }}</p>
          </header>

          <!-- 封面图 -->
          <div v-if="news.image_url" class="article-cover">
            <img :src="news.image_url" :alt="news.title" />
          </div>

          <!-- 文章正文 -->
          <div class="article-body" v-html="formattedContent"></div>

          <!-- 文章底部 -->
          <footer class="article-footer">
            <div class="share-section">
              <span class="share-label">分享到：</span>
              <div class="share-buttons">
                <button class="share-btn wechat" @click="shareToWechat" title="分享到微信">
                  <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M8.691 2.188C3.891 2.188 0 5.476 0 9.53c0 2.212 1.17 4.203 3.002 5.55a.59.59 0 0 1 .213.665l-.39 1.48c-.019.07-.048.141-.048.213 0 .163.13.295.29.295a.326.326 0 0 0 .167-.054l1.903-1.114a.864.864 0 0 1 .717-.098 10.16 10.16 0 0 0 2.837.403c.276 0 .543-.027.811-.05-.857-2.578.157-4.972 1.932-6.446 1.703-1.415 3.882-1.98 5.853-1.838-.576-3.583-4.196-6.348-8.596-6.348zM5.785 5.991c.642 0 1.162.529 1.162 1.18a1.17 1.17 0 0 1-1.162 1.178A1.17 1.17 0 0 1 4.623 7.17c0-.651.52-1.18 1.162-1.18zm5.813 0c.642 0 1.162.529 1.162 1.18a1.17 1.17 0 0 1-1.162 1.178 1.17 1.17 0 0 1-1.162-1.178c0-.651.52-1.18 1.162-1.18zm5.34 2.867c-1.797-.052-3.746.512-5.28 1.786-1.72 1.428-2.687 3.72-1.78 6.22.942 2.453 3.666 4.229 6.884 4.229.826 0 1.622-.12 2.361-.336a.722.722 0 0 1 .598.082l1.584.926a.272.272 0 0 0 .14.045c.134 0 .24-.111.24-.247 0-.06-.023-.12-.038-.177l-.327-1.233a.582.582 0 0 1-.023-.156.49.49 0 0 1 .201-.398C23.024 18.48 24 16.82 24 14.98c0-3.21-2.931-5.837-6.656-6.088V8.89c-.135-.01-.27-.027-.407-.03zm-2.53 3.274c.535 0 .969.44.969.982a.976.976 0 0 1-.969.983.976.976 0 0 1-.969-.983c0-.542.434-.982.97-.982zm4.844 0c.535 0 .969.44.969.982a.976.976 0 0 1-.969.983.976.976 0 0 1-.969-.983c0-.542.434-.982.969-.982z"/>
                  </svg>
                </button>
                <button class="share-btn weibo" @click="shareToWeibo" title="分享到微博">
                  <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M10.098 20.323c-3.977.391-7.414-1.406-7.672-4.02-.259-2.609 2.759-5.047 6.74-5.441 3.979-.394 7.413 1.404 7.671 4.018.259 2.6-2.759 5.049-6.739 5.443zM9.05 17.219c-.384.616-1.208.884-1.829.602-.612-.279-.793-.991-.406-1.593.379-.595 1.176-.861 1.793-.601.622.263.82.972.442 1.592zm1.27-1.627c-.141.237-.449.353-.689.253-.236-.09-.313-.361-.177-.586.138-.227.436-.346.672-.24.239.09.315.36.194.573zm.176-2.719c-1.893-.493-4.033.45-4.857 2.118-.836 1.704-.026 3.591 1.886 4.21 1.983.64 4.318-.341 5.132-2.179.8-1.793-.201-3.642-2.161-4.149zm7.563-1.224c-.346-.105-.579-.18-.405-.649.388-1.037.428-1.929.002-2.566-.801-1.196-2.994-1.129-5.535-.041l.001.001c-.357.148-.637-.089-.498-.406.27-.63.234-1.157-.113-1.463-.786-.686-2.872-.065-4.667 1.384-1.348 1.084-2.107 2.24-2.107 3.236 0 1.902 2.449 3.063 4.844 3.063 3.139 0 5.225-1.824 5.225-3.276 0-.877-.704-1.372-1.373-1.654l-.002.001c.851-.063 1.755.12 2.267.812.501.672.439 1.537-.072 2.407-.233.397.029.564.361.665.942.285 1.641.799 1.641 1.677 0 2.553-3.389 5.477-9.108 5.477-4.747 0-8.592-2.357-8.592-5.256 0-1.517.877-3.265 2.394-4.921 2.022-2.208 4.646-3.595 6.217-3.187.768.199 1.141.912.946 2.017l.002-.001c-.053.3.161.517.474.41.764-.26 1.399-.39 1.929-.393.501-.003.923.098 1.253.322.975.665 1.014 2.157.191 3.785-.202.401.123.543.368.626.982.337 1.682.873 1.682 1.804 0 1.806-2.222 4.199-7.006 4.199-3.788 0-6.913-1.642-6.913-4.241 0-1.355.814-2.914 2.232-4.377 1.893-1.946 4.098-3.02 5.326-2.611.562.187.868.684.774 1.398l-.001-.001c-.065.434.246.755.622.674.377-.08.71-.108.992-.079.768.073 1.293.427 1.293 1.069 0 1.256-1.792 2.852-5.006 2.852-2.104 0-3.907-.801-3.907-2.176 0-.722.483-1.536 1.32-2.297l-.001-.001c1.141-1.037 2.651-1.702 3.597-1.503.47.099.765.423.765.931 0 .635-.426 1.227-.986 1.527l-.002.001c-.153.082-.221.285-.1.437.122.153.362.185.536.075.724-.454 1.22-1.316 1.22-2.058 0-.88-.529-1.531-1.397-1.714-1.293-.273-3.11.499-4.465 1.727-1.016.922-1.574 1.9-1.574 2.713 0 1.788 2.146 2.962 4.673 2.962 3.551 0 5.789-1.877 5.789-3.541 0-.746-.556-1.271-1.422-1.565l-.001-.001z"/>
                  </svg>
                </button>
              </div>
            </div>
            
            <router-link :to="localePath('/news')" class="back-link">
              ← 返回新闻列表
            </router-link>
          </footer>
        </article>

        <!-- 相关新闻 -->
        <section v-if="relatedNews.length > 0" class="related-news">
          <h2>相关新闻</h2>
          <div class="related-list">
            <router-link 
              v-for="item in relatedNews" 
              :key="item.id"
              :to="localePath(`/news/detail/${item.id}`)"
              class="related-item"
            >
              <div class="related-image">
                <img :src="item.image_url || defaultImage" :alt="item.title" loading="lazy" />
              </div>
              <div class="related-info">
                <h3>{{ item.title }}</h3>
                <span class="related-date">{{ formatDate(item.published_at || item.created_at) }}</span>
              </div>
            </router-link>
          </div>
        </section>
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
const error = ref(null)
const news = ref(null)
const relatedNews = ref([])

// 判断是否为预览模式
const isPreviewMode = computed(() => {
  return !!route.query.token
})

// 格式化日期
const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

// 格式化内容（处理换行等）
const formattedContent = computed(() => {
  if (!news.value?.content) return ''
  // 将换行转为段落
  return news.value.content
    .split('\n\n')
    .filter(p => p.trim())
    .map(p => `<p>${p.replace(/\n/g, '<br>')}</p>`)
    .join('')
})

// 加载新闻详情
const loadNewsDetail = async () => {
  loading.value = true
  error.value = null
  
  try {
    const newsId = route.params.id
    const token = route.query.token
    
    let response
    if (token) {
      // 预览模式
      response = await axios.get(`/api/v1/news/preview/${token}`)
    } else {
      // 正常模式
      response = await axios.get(`/api/v1/news/detail/${newsId}`)
    }
    
    news.value = response.data
    
    // 加载相关新闻（同分类的其他新闻）
    if (!token) {
      await loadRelatedNews(news.value.category, newsId)
    }
  } catch (err) {
    console.error('加载新闻详情失败:', err)
    if (err.response?.status === 404) {
      error.value = '新闻不存在或未发布'
    } else {
      error.value = '加载失败，请稍后重试'
    }
  } finally {
    loading.value = false
  }
}

// 加载相关新闻
const loadRelatedNews = async (category, excludeId) => {
  try {
    const response = await axios.get('/api/v1/news/list', {
      params: { category, limit: 3 }
    })
    relatedNews.value = response.data
      .filter(item => item.id !== excludeId)
      .slice(0, 3)
  } catch (err) {
    console.error('加载相关新闻失败:', err)
  }
}

// 分享功能
const shareToWechat = () => {
  // 微信分享需要使用微信 JS-SDK，这里简单提示
  alert('请使用微信扫一扫功能分享此页面')
}

const shareToWeibo = () => {
  const url = encodeURIComponent(window.location.href)
  const title = encodeURIComponent(news.value?.title || '')
  window.open(`https://service.weibo.com/share/share.php?url=${url}&title=${title}`, '_blank')
}

// 监听路由变化
watch(() => route.params.id, () => {
  if (route.params.id) {
    loadNewsDetail()
  }
})

onMounted(() => {
  loadNewsDetail()
})
</script>

<style lang="scss" scoped>
.page-header {
  position: relative;
  height: 200px;
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
      margin-bottom: 16px;
      flex-wrap: wrap;
      
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
        max-width: 300px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }
    }
    
    h1 {
      font-size: 32px;
      font-weight: 600;
      color: #333;
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

.detail-content {
  padding: 60px 0;
  background: #f8f9fa;

  .loading-state,
  .error-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 400px;
    background: white;
    border-radius: 12px;
    
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
    
    .back-link {
      margin-top: 20px;
      color: #2CB5BE;
      text-decoration: none;
      
      &:hover {
        text-decoration: underline;
      }
    }
  }
}

.news-article {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
  
  .article-header {
    padding: 40px 40px 30px;
    
    .article-meta {
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 20px;
      
      .category-tag {
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 13px;
        color: white;
        
        &.company {
          background: #2CB5BE;
        }
        
        &.exhibition {
          background: #f59e0b;
        }
      }
      
      .publish-date {
        color: #999;
        font-size: 14px;
      }
    }
    
    .article-title {
      font-size: 28px;
      font-weight: 600;
      color: #333;
      line-height: 1.4;
      margin-bottom: 16px;
    }
    
    .article-summary {
      font-size: 16px;
      color: #666;
      line-height: 1.8;
      padding: 16px 20px;
      background: #f8f9fa;
      border-left: 4px solid #2CB5BE;
      border-radius: 0 8px 8px 0;
    }
  }
  
  .article-cover {
    padding: 0 40px;
    
    img {
      width: 100%;
      max-height: 500px;
      object-fit: cover;
      border-radius: 8px;
    }
  }
  
  .article-body {
    padding: 30px 40px 40px;
    font-size: 16px;
    color: #333;
    line-height: 1.9;
    
    :deep(p) {
      margin-bottom: 20px;
      
      &:last-child {
        margin-bottom: 0;
      }
    }
    
    :deep(img) {
      max-width: 100%;
      border-radius: 8px;
      margin: 20px 0;
    }
  }
  
  .article-footer {
    padding: 30px 40px;
    border-top: 1px solid #eee;
    display: flex;
    justify-content: space-between;
    align-items: center;
    
    .share-section {
      display: flex;
      align-items: center;
      gap: 12px;
      
      .share-label {
        color: #666;
        font-size: 14px;
      }
      
      .share-buttons {
        display: flex;
        gap: 10px;
        
        .share-btn {
          width: 36px;
          height: 36px;
          border-radius: 50%;
          border: none;
          cursor: pointer;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: all 0.3s;
          
          svg {
            width: 20px;
            height: 20px;
          }
          
          &.wechat {
            background: #07c160;
            color: white;
            
            &:hover {
              background: #06ad56;
            }
          }
          
          &.weibo {
            background: #e6162d;
            color: white;
            
            &:hover {
              background: #cc1427;
            }
          }
        }
      }
    }
    
    .back-link {
      color: #2CB5BE;
      text-decoration: none;
      font-size: 15px;
      transition: all 0.3s;
      
      &:hover {
        color: #1a8a91;
      }
    }
  }
}

.related-news {
  margin-top: 50px;
  
  h2 {
    font-size: 22px;
    color: #333;
    margin-bottom: 24px;
    padding-left: 12px;
    border-left: 4px solid #2CB5BE;
  }
  
  .related-list {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
  }
  
  .related-item {
    background: white;
    border-radius: 10px;
    overflow: hidden;
    text-decoration: none;
    transition: all 0.3s;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    
    &:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
      
      .related-image img {
        transform: scale(1.05);
      }
    }
    
    .related-image {
      height: 160px;
      overflow: hidden;
      
      img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s;
      }
    }
    
    .related-info {
      padding: 16px;
      
      h3 {
        font-size: 15px;
        color: #333;
        line-height: 1.5;
        margin-bottom: 8px;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
      }
      
      .related-date {
        font-size: 13px;
        color: #999;
      }
    }
  }
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@media (max-width: 992px) {
  .related-news .related-list {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .page-header {
    height: 160px;
    
    .header-content {
      padding: 0 15px;
      
      .breadcrumb {
        font-size: 12px;
      }
      
      h1 {
        font-size: 24px;
      }
    }
  }
  
  .news-article {
    .article-header {
      padding: 24px 20px 20px;
      
      .article-title {
        font-size: 22px;
      }
      
      .article-summary {
        font-size: 14px;
        padding: 12px 16px;
      }
    }
    
    .article-cover {
      padding: 0 20px;
    }
    
    .article-body {
      padding: 20px;
      font-size: 15px;
    }
    
    .article-footer {
      padding: 20px;
      flex-direction: column;
      gap: 20px;
      align-items: flex-start;
    }
  }
  
  .related-news .related-list {
    grid-template-columns: 1fr;
  }
}
</style>
