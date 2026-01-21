<template>
  <div class="news-page">
    <!-- 页面头部 Banner（包含面包屑导航） -->
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
          <span class="current">{{ t('newsPage.title') }}</span>
        </nav>
        <h1>{{ t('newsPage.title') }}</h1>
        <p>{{ t('newsPage.subtitle') }}</p>
      </div>
    </div>

    <section class="news-content">
      <div class="container">
        <div class="news-list">
          <div 
            class="news-item card" 
            v-for="item in newsList" 
            :key="item.id"
          >
            <div class="news-image">
              <img :src="item.image" :alt="item.title" loading="lazy" />
            </div>
            <div class="news-info">
              <div class="news-meta">
                <span class="news-date">{{ item.date }}</span>
              </div>
              <h3>{{ item.title }}</h3>
              <p>{{ item.summary }}</p>
              <a href="#" class="read-more">{{ t('newsPage.readMore') }}</a>
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
import news1 from '@/assets/images/news/news1.jpg'
import news2 from '@/assets/images/news/news2.jpg'
import news3 from '@/assets/images/news/news3.jpg'

const { t, localePath } = useLocale()

const headerBg = ref(bgImage)

const newsList = [
  {
    id: 1,
    title: '2019年上海国际工业装配与传输技术展览会',
    summary: '2019年上海国际工业装配与传输技术展览会，将于2019年7月在上海举行。泰田集团将携旗下核心产品亮相展会，展示公司在工业装配领域的最新技术成果和解决方案。',
    date: '2020-04-11',
    image: news1
  },
  {
    id: 2,
    title: '泰田集团喜获"浙江名牌产品"称号',
    summary: '"浙江名牌"荣誉是经区、市级质量监督管理部门严格审核通过，由浙江省质量技术监督局认定授予的称号。泰田集团凭借卓越的产品质量和良好的市场口碑荣获此殊荣。',
    date: '2018-10-29',
    image: news2
  },
  {
    id: 3,
    title: '《冲击式气扳机》"浙江制造"团体标准评审会在我司召开',
    summary: '"浙江制造"是浙江省启动的将"浙江制造"打造成为具有严格认证要求的区域公共品牌的重要举措。本次评审会的召开标志着泰田集团在行业标准制定方面迈出重要一步。',
    date: '2020-04-11',
    image: news3
  },
  {
    id: 4,
    title: '泰田集团通过浙江省省级企业研究院认定',
    summary: '省科技厅近日公布了2018年省级企业研究院认定名单，泰田集团榜上有名。这标志着公司的研发创新能力得到了省级认可，将进一步推动公司技术创新和产品升级。',
    date: '2018-10-19',
    image: news1
  },
  {
    id: 5,
    title: '泰田集团参加2018年秋季校园招聘会',
    summary: '"问渠哪得清如许，为有源头活水来"，一个公司要发展壮大、团队要永葆活力，就需要不断注入新鲜血液。泰田集团积极参与校园招聘，为公司发展储备优秀人才。',
    date: '2020-04-11',
    image: news2
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

.news-content {
  padding: 80px 0;
  background: #f8f9fa;

  .news-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
    gap: 30px;
  }

  .news-item {
    display: flex;
    flex-direction: column;
    background: white;
    border-radius: 12px;
    overflow: hidden;
    transition: all 0.3s;
    
    &:hover {
      transform: translateY(-8px);
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.12);
      
      .news-image img {
        transform: scale(1.05);
      }
    }

    .news-image {
      height: 200px;
      overflow: hidden;
      
      img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s;
      }
    }

    .news-info {
      padding: 25px;
      flex: 1;
      display: flex;
      flex-direction: column;
      
      .news-meta {
        margin-bottom: 12px;
      }

      .news-date {
        font-size: 13px;
        color: #2CB5BE;
        font-weight: 500;
      }

      h3 {
        font-size: 18px;
        color: #333;
        margin-bottom: 12px;
        line-height: 1.5;
        transition: color 0.3s;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;

        &:hover {
          color: #2CB5BE;
        }
      }

      p {
        font-size: 14px;
        color: #666;
        line-height: 1.7;
        margin-bottom: 15px;
        flex: 1;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
      }

      .read-more {
        color: #2CB5BE;
        text-decoration: none;
        font-size: 14px;
        font-weight: 500;
        transition: all 0.3s;
        display: inline-block;

        &:hover {
          color: #1a8a91;
          transform: translateX(5px);
        }
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
  
  .news-content .news-list {
    grid-template-columns: 1fr;
  }
}
</style>
