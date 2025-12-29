<template>
  <div class="about-page">
    <div class="page-header">
      <div class="container">
        <h1>关于泰田</h1>
        <p>专注于工业制造领域的创新与发展</p>
      </div>
    </div>

    <section class="about-content">
      <div class="container">
        <div class="content-section">
          <h2>企业信息</h2>
          <p>泰田集团股份有限公司成立于2007年，注册资金6088万元，现拥有员工900余人，是一家集研发、生产与销售为一体的高新技术企业，也是"专精特新"小巨人企业。</p>
          <p>公司始终坚信先进的装备是一流品质的保障，引进国外先进生产线，并配备2000多台CNC加工设备，全面部署MES+ERP系统，实现人机信息的高度一体化。</p>
        </div>

        <div class="content-section">
          <h2>企业理念</h2>
          <div class="philosophy-grid">
            <div class="philosophy-item card">
              <h3>创新</h3>
              <p>坚持自主创新，打造行业知识产权高地</p>
            </div>
            <div class="philosophy-item card">
              <h3>品质</h3>
              <p>先进装备保障一流品质</p>
            </div>
            <div class="philosophy-item card">
              <h3>服务</h3>
              <p>为客户创造效益，提供优质服务</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
</script>

<style lang="scss" scoped>
.page-header {
  background: linear-gradient(135deg, #2CB5BE 0%, #1a8a91 100%);
  color: white;
  padding: 80px 0;
  text-align: center;

  h1 {
    font-size: 48px;
    margin-bottom: 15px;
  }

  p {
    font-size: 20px;
    opacity: 0.9;
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
      line-height: 1.8;
      color: #666;
      margin-bottom: 20px;
    }
  }

  .philosophy-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
    margin-top: 40px;
  }

  .philosophy-item {
    padding: 40px 30px;
    text-align: center;

    h3 {
      font-size: 24px;
      color: #2CB5BE;
      margin-bottom: 15px;
    }

    p {
      font-size: 15px;
      color: #666;
      line-height: 1.6;
      margin: 0;
    }
  }
}
</style>

