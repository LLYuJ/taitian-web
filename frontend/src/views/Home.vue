<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="hero">
      <img 
        :src="heroBannerUrl" 
        alt="泰田集团产品展示" 
        class="hero-bg"
        @load="onHeroLoad"
      />
      <div class="hero-overlay"></div>
      <div class="container hero-container">
        <div class="hero-content">
          <h1 class="hero-title">{{ t('home.heroTitle') }}</h1>
          <p class="hero-subtitle">{{ t('home.heroSubtitle') }}</p>
          <router-link :to="localePath('/products')" class="industrial-button">{{ t('home.viewProducts') }}</router-link>
        </div>
      </div>
    </section>

    <!-- Company Intro -->
    <section class="company-intro">
      <div class="container">
        <div class="intro-content">
          <p class="intro-text">
            {{ t('home.companyIntro.description') }}
          </p>
        </div>

        <!-- 企业信息统计 -->
        <div class="stats-showcase" ref="statsRef">
          <div class="stat-item" v-for="(stat, index) in companyStats" :key="stat.labelKey">
            <div class="stat-number-wrapper">
              <span class="stat-number">{{ animatedValues[index] }}</span>
              <span class="stat-unit">{{ stat.unit }}</span>
            </div>
            <div class="stat-label">{{ t(stat.labelKey) }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Research Section -->
    <section class="research-section">
      <div class="container">
        <p class="research-intro">
          {{ t('home.research.intro') }}
        </p>
        
        <div class="research-grid">
          <div class="research-card" v-for="item in researchItems" :key="item.titleKey">
            <div class="research-image">
              <img :src="item.image" :alt="t(item.titleKey)" loading="lazy" />
            </div>
            <div class="research-info">
              <h3>{{ t(item.titleKey) }}</h3>
              <p>{{ t(item.descKey) }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Products -->
    <section class="products-section">
      <div class="container">
        <h2 class="section-title">{{ t('home.products.title') }}</h2>
        <p class="section-subtitle">{{ t('home.products.subtitle') }}</p>

        <div class="products-grid">
          <div class="product-card card" v-for="product in products" :key="product.nameKey">
            <div class="product-image">
              <img :src="product.image" :alt="t(product.nameKey)" loading="lazy" />
            </div>
            <h3>{{ t(product.nameKey) }}</h3>
            <p>{{ t(product.descKey) }}</p>
          </div>
        </div>
        
        <div class="products-action">
          <router-link :to="localePath('/products')" class="industrial-button">{{ t('home.products.viewAll') }}</router-link>
        </div>
      </div>
    </section>

    <!-- News Section -->
    <section class="news-section">
      <div class="container">
        <h2 class="section-title">{{ t('home.news.title') }}</h2>
        <div class="news-grid">
          <div class="news-card" v-for="news in newsList" :key="news.id">
            <div class="news-image">
              <img :src="news.image" :alt="news.title" loading="lazy" />
            </div>
            <div class="news-info">
              <h3>{{ news.title }}</h3>
              <p>{{ news.summary }}</p>
              <span class="news-date">{{ news.date }}</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <div class="container">
        <h2>{{ t('home.cta.title') }}</h2>
        <p>{{ t('home.cta.subtitle') }}</p>
        <div class="phone-number">{{ t('home.cta.phone') }}</div>
        <router-link :to="localePath('/contact')" class="industrial-button cta-btn">{{ t('home.cta.consult') }}</router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, reactive } from 'vue'
import { useLocale } from '@/composables/useLocale'

// 引入图片
import heroBanner from '@/assets/images/banners/new_factory.png'
import researchConcept from '@/assets/images/banners/research-concept.jpg'
import researchPractice from '@/assets/images/banners/research-practice.jpg'
import researchResource from '@/assets/images/banners/research-resource.jpg'
import precisionMachine from '@/assets/images/products/precision-machine.png'
import screwCompressor from '@/assets/images/products/screw-compressor.jpg'
import industrialWrench from '@/assets/images/products/industrial-wrench.jpg'
import autoRepairTools from '@/assets/images/products/auto-repair-tools.png'
import news1 from '@/assets/images/news/news1.jpg'
import news2 from '@/assets/images/news/news2.jpg'
import news3 from '@/assets/images/news/news3.jpg'

const { t, localePath } = useLocale()

const heroBannerUrl = ref(heroBanner)

// 企业统计数据 - 包含数字值和单位分离
const companyStats = [
  { numericValue: 2007, unit: '年', labelKey: 'home.stats.foundedIn', static: true }, // 年份不需要动画
  { numericValue: 6088, unit: '万', labelKey: 'home.stats.registeredCapital' },
  { numericValue: 900, unit: '+', labelKey: 'home.stats.employees' },
  { numericValue: 2000, unit: '+', labelKey: 'home.stats.cncEquipment' },
  { numericValue: 120, unit: '+', labelKey: 'home.stats.patents' },
  { numericValue: 20, unit: '万', labelKey: 'home.stats.compressorHosts' },
  { numericValue: 100, unit: '万', labelKey: 'home.stats.pneumaticTools' }
]

// 动画相关
const statsRef = ref(null)
// 静态数字直接显示最终值，其他初始化为 0
const animatedValues = reactive(companyStats.map(stat => stat.static ? stat.numericValue : 0))
let hasAnimated = false
let observer = null

// 数字递增动画函数
const animateNumber = (index, targetValue, duration = 2000) => {
  const startTime = performance.now()
  const startValue = 0
  
  const easeOutQuart = (t) => 1 - Math.pow(1 - t, 4)
  
  const updateNumber = (currentTime) => {
    const elapsed = currentTime - startTime
    const progress = Math.min(elapsed / duration, 1)
    const easedProgress = easeOutQuart(progress)
    
    animatedValues[index] = Math.floor(startValue + (targetValue - startValue) * easedProgress)
    
    if (progress < 1) {
      requestAnimationFrame(updateNumber)
    } else {
      animatedValues[index] = targetValue
    }
  }
  
  requestAnimationFrame(updateNumber)
}

// 启动所有数字动画
const startCountAnimation = () => {
  if (hasAnimated) return
  hasAnimated = true
  
  companyStats.forEach((stat, index) => {
    // 跳过静态数字（如年份）
    if (stat.static) return
    
    // 添加延迟让动画有层次感
    setTimeout(() => {
      animateNumber(index, stat.numericValue, 2000)
    }, index * 100)
  })
}

// Intersection Observer 回调
const handleIntersection = (entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      startCountAnimation()
    }
  })
}

onMounted(() => {
  // 创建 Intersection Observer
  observer = new IntersectionObserver(handleIntersection, {
    threshold: 0.3,
    rootMargin: '0px'
  })
  
  if (statsRef.value) {
    observer.observe(statsRef.value)
  }
})

onUnmounted(() => {
  if (observer) {
    observer.disconnect()
  }
})

const researchItems = [
  { 
    titleKey: 'home.research.concept', 
    descKey: 'home.research.conceptDesc',
    image: researchConcept
  },
  { 
    titleKey: 'home.research.practice', 
    descKey: 'home.research.practiceDesc',
    image: researchPractice
  },
  { 
    titleKey: 'home.research.resource', 
    descKey: 'home.research.resourceDesc',
    image: researchResource
  }
]

const products = [
  { nameKey: 'home.products.precisionMachine', descKey: 'home.products.precisionMachineDesc', image: precisionMachine },
  { nameKey: 'home.products.screwCompressor', descKey: 'home.products.screwCompressorDesc', image: screwCompressor },
  { nameKey: 'home.products.industrialWrench', descKey: 'home.products.industrialWrenchDesc', image: industrialWrench },
  { nameKey: 'home.products.autoRepairTools', descKey: 'home.products.autoRepairToolsDesc', image: autoRepairTools }
]

const newsList = [
  { 
    id: 1, 
    title: '2019年上海国际工业装配与传输技术展览会', 
    summary: '2019年上海国际工业装配与传输技术展览会，将于2019年7月...',
    date: '2020-04-11',
    image: news1
  },
  { 
    id: 2, 
    title: '泰田集团喜获"浙江名牌产品"称号', 
    summary: '"浙江名牌"荣誉是经区、市级质量监督管理部门严格审核通过...',
    date: '2018-10-29',
    image: news2
  },
  { 
    id: 3, 
    title: '《冲击式气扳机》"浙江制造"团体标准评审会在我司召开', 
    summary: '"浙江制造"是浙江省启动的将"浙江制造"打造成为具有严格认证...',
    date: '2020-04-11',
    image: news3
  }
]

const onHeroLoad = () => {
  console.log('Hero image loaded')
}
</script>

<style lang="scss" scoped>
.hero {
  height: 50vh;
  min-height: 400px;
  max-height: 500px;
  position: relative;
  color: white;
  overflow: hidden;

  .hero-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    z-index: 0;
  }

  .hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(90deg, rgba(0, 0, 0, 0.6) 0%, rgba(0, 0, 0, 0.3) 50%, transparent 100%);
    z-index: 1;
  }

  .hero-container {
    position: relative;
    z-index: 2;
    height: 100%;
    display: flex;
    align-items: center;
  }

  .hero-content {
    text-align: left;
    max-width: 600px;
    padding: 40px 0;
  }

  .hero-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 16px;
    line-height: 1.2;
    letter-spacing: 2px;
  }

  .hero-subtitle {
    font-size: 18px;
    margin-bottom: 32px;
    opacity: 0.95;
    line-height: 1.6;
    font-weight: 400;
  }
  
  .industrial-button {
    text-decoration: none;
    display: inline-block;
  }
}

.company-intro {
  padding: 50px 0 40px;
  background: white;

  .intro-content {
    max-width: 1000px;
    margin: 0 auto 30px;
  }

  .intro-text {
    font-size: 15px;
    line-height: 1.8;
    color: #666;
    text-align: center;
  }
}

// 企业信息统计展示区
.stats-showcase {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 50px 60px;
  margin: 30px 0 0;
  background: linear-gradient(
    180deg,
    #f8f9fa 0%,
    #f2f4f6 50%,
    #eef0f2 100%
  );
  background-image: 
    linear-gradient(180deg, #f8f9fa 0%, #f2f4f6 50%, #eef0f2 100%),
    url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23e0e3e6' fill-opacity='0.15'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
  border-radius: 0;
  position: relative;
  overflow: hidden;
  
  // 右下角装饰性背景
  &::after {
    content: '';
    position: absolute;
    right: 0;
    bottom: 0;
    width: 40%;
    height: 100%;
    background: linear-gradient(135deg, transparent 30%, rgba(0, 0, 0, 0.02) 100%);
    pointer-events: none;
  }
  
  .stat-item {
    flex: 1;
    text-align: center;
    padding: 20px 10px;
    position: relative;
    z-index: 1;
    
    // 分隔线效果
    &:not(:last-child)::after {
      content: '';
      position: absolute;
      right: 0;
      top: 50%;
      transform: translateY(-50%);
      width: 1px;
      height: 60px;
      background: linear-gradient(
        180deg,
        transparent 0%,
        rgba(0, 0, 0, 0.08) 50%,
        transparent 100%
      );
    }
  }
  
  .stat-number-wrapper {
    display: flex;
    align-items: flex-start;
    justify-content: center;
    margin-bottom: 12px;
    line-height: 1;
  }
  
  .stat-number {
    font-size: 42px;
    font-weight: 700;
    color: #1a1a1a;
    font-family: 'DIN Alternate', 'Oswald', 'Bebas Neue', 'Arial Black', sans-serif;
    letter-spacing: -1px;
  }
  
  .stat-unit {
    font-size: 20px;
    font-weight: 400;
    color: #333;
    margin-left: 4px;
    margin-top: 6px;
    font-family: inherit;
  }
  
  .stat-label {
    font-size: 15px;
    color: #555;
    font-weight: 400;
    letter-spacing: 0.5px;
  }
}

@media (max-width: 1200px) {
  .stats-showcase {
    padding: 60px 30px;
    flex-wrap: wrap;
    gap: 30px;
    
    .stat-item {
      flex: 0 0 calc(25% - 22.5px);
      
      &::after {
        display: none;
      }
    }
    
    .stat-number {
      font-size: 36px;
    }
  }
}

@media (max-width: 768px) {
  .stats-showcase {
    padding: 50px 20px;
    gap: 25px;
    
    .stat-item {
      flex: 0 0 calc(50% - 12.5px);
    }
    
    .stat-number {
      font-size: 28px;
    }
    
    .stat-unit {
      font-size: 14px;
    }
    
    .stat-label {
      font-size: 13px;
    }
  }
}

@media (max-width: 480px) {
  .stats-showcase {
    .stat-item {
      flex: 0 0 100%;
    }
  }
}

.research-section {
  padding: 80px 0;
  background: linear-gradient(180deg, #f8f9fa 0%, #fff 100%);
  
  .research-intro {
    max-width: 900px;
    margin: 0 auto 50px;
    text-align: center;
    font-size: 16px;
    line-height: 1.8;
    color: #666;
  }
  
  .research-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
  }
  
  .research-card {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    transition: all 0.3s;
    
    &:hover {
      transform: translateY(-8px);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
    }
    
    .research-image {
      height: 200px;
      overflow: hidden;
      
      img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s;
      }
    }
    
    &:hover .research-image img {
      transform: scale(1.05);
    }
    
    .research-info {
      padding: 25px;
      text-align: center;
      
      h3 {
        font-size: 20px;
        color: #2CB5BE;
        margin-bottom: 10px;
      }
      
      p {
        font-size: 14px;
        color: #666;
      }
    }
  }
}

.products-section {
  padding: 80px 0;
  background: #f8f9fa;

  .products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 30px;
  }

  .product-card {
    padding: 30px;
    text-align: center;
    background: white;

    .product-image {
      width: 100%;
      height: 180px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 20px;
      overflow: hidden;
      
      img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
        transition: transform 0.3s;
      }
    }
    
    &:hover .product-image img {
      transform: scale(1.08);
    }

    h3 {
      font-size: 18px;
      color: #333;
      margin-bottom: 12px;
    }

    p {
      font-size: 14px;
      color: #666;
      line-height: 1.6;
    }
  }
  
  .products-action {
    text-align: center;
    margin-top: 50px;
    
    .industrial-button {
      text-decoration: none;
    }
  }
}

.news-section {
  padding: 80px 0;
  background: white;
  
  .news-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    margin-top: 50px;
  }
  
  .news-card {
    background: #f8f9fa;
    border-radius: 12px;
    overflow: hidden;
    transition: all 0.3s;
    
    &:hover {
      transform: translateY(-5px);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }
    
    .news-image {
      height: 180px;
      overflow: hidden;
      
      img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s;
      }
    }
    
    &:hover .news-image img {
      transform: scale(1.05);
    }
    
    .news-info {
      padding: 20px;
      
      h3 {
        font-size: 16px;
        color: #333;
        margin-bottom: 10px;
        line-height: 1.5;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
      }
      
      p {
        font-size: 14px;
        color: #666;
        line-height: 1.6;
        margin-bottom: 10px;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
      }
      
      .news-date {
        font-size: 12px;
        color: #999;
      }
    }
  }
}

.cta-section {
  padding: 80px 0;
  background: linear-gradient(135deg, #1a8a91 0%, #2CB5BE 100%);
  color: white;
  text-align: center;

  h2 {
    font-size: 36px;
    margin-bottom: 10px;
  }

  p {
    font-size: 18px;
    margin-bottom: 20px;
    opacity: 0.9;
  }

  .phone-number {
    font-size: 48px;
    font-weight: 700;
    margin: 30px 0;
    letter-spacing: 2px;
  }

  .cta-btn {
    background: white;
    color: #2CB5BE;
    text-decoration: none;
    
    &:hover {
      background: #f0f0f0;
    }
  }
}

@media (max-width: 992px) {
  .research-section .research-grid,
  .news-section .news-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .hero {
    height: 45vh;
    min-height: 320px;

    .hero-content {
      padding: 30px 0;
    }

    .hero-title {
      font-size: 28px;
      letter-spacing: 1px;
    }

    .hero-subtitle {
      font-size: 14px;
      margin-bottom: 24px;
    }
  }
  
  .research-section .research-grid,
  .news-section .news-grid {
    grid-template-columns: 1fr;
  }

  .products-section .products-grid {
    grid-template-columns: 1fr;
  }

  .cta-section .phone-number {
    font-size: 32px;
  }
}
</style>
