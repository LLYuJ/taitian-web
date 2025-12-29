<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1 class="hero-title">拧紧工具/空气动力设备解决方案服务商</h1>
        <p class="hero-subtitle">专精特新 · 智能制造 · 品质保障</p>
        <button class="industrial-button">了解更多</button>
      </div>
      <div class="hero-overlay"></div>
    </section>

    <!-- Company Intro -->
    <section class="company-intro">
      <div class="container">
        <h2 class="section-title">专精特新</h2>
        <p class="section-subtitle">高新技术企业 · 专精特新小巨人企业</p>
        
        <div class="intro-content">
          <p class="intro-text">
            泰田集团股份有限公司成立于2007年，注册资金6088万元，现拥有员工900余人，
            是一家集研发、生产与销售为一体的高新技术企业，也是"专精特新"小巨人企业。
            拥有精密机床/空气压缩机、压缩机主机、拧紧工具以及精密机械零件加工三大生产基地。
          </p>
        </div>

        <div class="stats">
          <div class="stat-item">
            <div class="stat-number">2007</div>
            <div class="stat-label">公司创立于</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">6088万</div>
            <div class="stat-label">公司注册资金</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">900+</div>
            <div class="stat-label">公司员工数</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">2000+</div>
            <div class="stat-label">CNC加工设备</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">120+</div>
            <div class="stat-label">公司专利数</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">20万</div>
            <div class="stat-label">年产压缩主机</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Products -->
    <section class="products-section">
      <div class="container">
        <h2 class="section-title">产品中心</h2>
        <p class="section-subtitle">为客户提供优质的产品与服务</p>

        <div class="products-grid">
          <div class="product-card card">
            <div class="product-icon">🔧</div>
            <h3>精密机床</h3>
            <p>高精度、高效率的精密机床设备</p>
          </div>
          <div class="product-card card">
            <div class="product-icon">⚙️</div>
            <h3>螺杆式空气压缩机</h3>
            <p>节能高效的空气压缩解决方案</p>
          </div>
          <div class="product-card card">
            <div class="product-icon">🔩</div>
            <h3>工业级扳手系列</h3>
            <p>专业的工业拧紧工具</p>
          </div>
          <div class="product-card card">
            <div class="product-icon">🛠️</div>
            <h3>汽修工具系列</h3>
            <p>全方位的汽修工具解决方案</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <div class="container">
        <h2>联系我们</h2>
        <p>全国售后服务热线</p>
        <div class="phone-number">400-826-1128</div>
        <button class="industrial-button">立即咨询</button>
      </div>
    </section>
  </div>
</template>

<script setup>
</script>

<style lang="scss" scoped>
.hero {
  height: 600px;
  background: linear-gradient(135deg, #2CB5BE 0%, #1a8a91 100%);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  overflow: hidden;

  .hero-content {
    text-align: center;
    position: relative;
    z-index: 2;
    padding: 0 20px;
  }

  .hero-title {
    font-size: 48px;
    font-weight: 700;
    margin-bottom: 20px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
  }

  .hero-subtitle {
    font-size: 24px;
    margin-bottom: 40px;
    opacity: 0.95;
  }

  .hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="grid" width="100" height="100" patternUnits="userSpaceOnUse"><path d="M 100 0 L 0 0 0 100" fill="none" stroke="white" stroke-width="0.5" opacity="0.1"/></pattern></defs><rect width="100%" height="100%" fill="url(%23grid)" /></svg>');
  }
}

.company-intro {
  padding: 80px 0;
  background: white;

  .intro-content {
    max-width: 900px;
    margin: 0 auto 60px;
  }

  .intro-text {
    font-size: 16px;
    line-height: 1.8;
    color: #666;
    text-align: center;
  }

  .stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 40px;
    margin-top: 60px;
  }

  .stat-item {
    text-align: center;
    padding: 30px 20px;
    border-radius: 8px;
    background: #f8f9fa;
    transition: all 0.3s;

    &:hover {
      background: #2CB5BE;
      transform: translateY(-5px);
      box-shadow: 0 8px 20px rgba(44, 181, 190, 0.3);

      .stat-number, .stat-label {
        color: white;
      }
    }
  }

  .stat-number {
    font-size: 36px;
    font-weight: 700;
    color: #2CB5BE;
    margin-bottom: 10px;
  }

  .stat-label {
    font-size: 14px;
    color: #666;
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
    padding: 40px 30px;
    text-align: center;
    background: white;

    .product-icon {
      font-size: 48px;
      margin-bottom: 20px;
    }

    h3 {
      font-size: 20px;
      color: #333;
      margin-bottom: 15px;
    }

    p {
      font-size: 14px;
      color: #666;
      line-height: 1.6;
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

  .industrial-button {
    background: white;
    color: #2CB5BE;
    
    &:hover {
      background: #f0f0f0;
    }
  }
}

@media (max-width: 768px) {
  .hero {
    height: 400px;

    .hero-title {
      font-size: 32px;
    }

    .hero-subtitle {
      font-size: 18px;
    }
  }

  .company-intro .stats {
    grid-template-columns: repeat(2, 1fr);
  }

  .products-section .products-grid {
    grid-template-columns: 1fr;
  }

  .cta-section .phone-number {
    font-size: 32px;
  }
}
</style>

