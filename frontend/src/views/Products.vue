<template>
  <div class="products-page">
    <!-- 页面头部 Banner（包含面包屑导航） -->
    <div class="page-header">
      <img 
        :src="headerBgImage" 
        alt="泰田产品展示" 
        class="header-bg"
        loading="eager"
      />
      <div class="header-content">
        <nav class="breadcrumb">
          <router-link :to="localePath('/')">{{ t('nav.home') }}</router-link>
          <span class="separator">&gt;</span>
          <span class="current">{{ t('productsPage.title') }}</span>
        </nav>
        <h1>{{ t('productsPage.title') }}</h1>
        <p>{{ t('productsPage.subtitle') }}</p>
      </div>
    </div>

    <section class="products-content">
      <div class="container">
        <div class="products-list">
          <div 
            class="product-item card" 
            v-for="product in products" 
            :key="product.nameKey"
          >
            <div class="product-image">
              <img 
                :src="product.image" 
                :alt="t(product.nameKey)" 
                loading="lazy"
              />
            </div>
            <div class="product-info">
              <h3>{{ t(product.nameKey) }}</h3>
              <p>{{ t(product.descKey) }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 工业之心 泰田智造 -->
    <section class="slogan-section">
      <div class="container">
        <h2 class="slogan-title">{{ t('productsPage.slogan') }}</h2>
        <div class="slogan-items">
          <p>{{ t('productsPage.sloganItem1') }}</p>
          <p>{{ t('productsPage.sloganItem2') }}</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useLocale } from '@/composables/useLocale'

// 引入图片
import headerBg from '@/assets/images/backgrounds/page-header-bg.jpg'
import precisionMachine from '@/assets/images/products/precision-machine.png'
import screwCompressor from '@/assets/images/products/screw-compressor.jpg'
import industrialWrench from '@/assets/images/products/industrial-wrench.jpg'
import compressorHost from '@/assets/images/products/compressor-host.jpg'
import autoRepairTools from '@/assets/images/products/auto-repair-tools.png'
import lubricationEquipment from '@/assets/images/products/lubrication-equipment.jpg'

const { t, localePath } = useLocale()

const headerBgImage = ref(headerBg)

const products = [
  { 
    nameKey: 'productsPage.items.precisionMachine', 
    descKey: 'productsPage.items.precisionMachineDesc',
    image: precisionMachine
  },
  { 
    nameKey: 'productsPage.items.screwCompressor', 
    descKey: 'productsPage.items.screwCompressorDesc',
    image: screwCompressor
  },
  { 
    nameKey: 'productsPage.items.industrialWrench', 
    descKey: 'productsPage.items.industrialWrenchDesc',
    image: industrialWrench
  },
  { 
    nameKey: 'productsPage.items.compressorHost', 
    descKey: 'productsPage.items.compressorHostDesc',
    image: compressorHost
  },
  { 
    nameKey: 'productsPage.items.autoRepairTools', 
    descKey: 'productsPage.items.autoRepairToolsDesc',
    image: autoRepairTools
  },
  { 
    nameKey: 'productsPage.items.lubricationEquipment', 
    descKey: 'productsPage.items.lubricationEquipmentDesc',
    image: lubricationEquipment
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

.products-content {
  padding: 80px 0;
  background: #f8f9fa;

  .products-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 30px;
  }

  .product-item {
    display: flex;
    flex-direction: column;
    background: white;
    border-radius: 12px;
    overflow: hidden;
    transition: all 0.3s;

    &:hover {
      transform: translateY(-8px);
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.12);
      
      .product-image img {
        transform: scale(1.05);
      }
    }

    .product-image {
      height: 220px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #f5f5f5;
      padding: 20px;
      overflow: hidden;
      
      img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
        transition: transform 0.5s;
      }
    }

    .product-info {
      padding: 25px;

      h3 {
        font-size: 20px;
        color: #333;
        margin-bottom: 12px;
      }

      p {
        font-size: 14px;
        color: #666;
        line-height: 1.7;
        margin: 0;
      }
    }
  }
}

.slogan-section {
  padding: 80px 0;
  background: linear-gradient(135deg, #2CB5BE 0%, #1a8a91 100%);
  text-align: center;
  color: white;
  
  .slogan-title {
    font-size: 36px;
    font-weight: 700;
    margin-bottom: 30px;
  }
  
  .slogan-items {
    p {
      font-size: 18px;
      opacity: 0.9;
      margin: 10px 0;
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
  
  .products-content .products-list {
    grid-template-columns: 1fr;
  }

  .product-item {
    flex-direction: column;
    text-align: center;
  }
  
  .slogan-section .slogan-title {
    font-size: 28px;
  }
}
</style>
