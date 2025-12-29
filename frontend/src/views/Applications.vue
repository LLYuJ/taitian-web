<template>
  <div class="applications-page">
    <div class="page-header">
      <div class="container">
        <h1>行业应用</h1>
        <p>为多个行业提供专业的解决方案</p>
      </div>
    </div>

    <section class="applications-content">
      <div class="container">
        <div class="applications-grid">
          <div class="application-card card">
            <div class="card-icon">🚗</div>
            <h3>汽车制造行业</h3>
            <p>为汽车制造行业提供专业的拧紧工具和空气动力解决方案，确保生产线的高效运行。</p>
          </div>

          <div class="application-card card">
            <div class="card-icon">⚙️</div>
            <h3>精密制造行业</h3>
            <p>高精度机床和精密加工设备，满足精密制造的严格要求。</p>
          </div>

          <div class="application-card card">
            <div class="card-icon">🤖</div>
            <h3>工业自动化行业</h3>
            <p>智能化、自动化的工业解决方案，助力企业实现智能制造。</p>
          </div>

          <div class="application-card card">
            <div class="card-icon">🔧</div>
            <h3>汽车维修行业</h3>
            <p>专业的汽修工具系列，提高维修效率和质量。</p>
          </div>

          <div class="application-card card">
            <div class="card-icon">💧</div>
            <h3>流体及汽车保养行业</h3>
            <p>润滑设备和流体处理解决方案，保障设备正常运行。</p>
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

.applications-content {
  padding: 80px 0;
  background: white;

  .applications-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
  }

  .application-card {
    padding: 40px 30px;
    text-align: center;

    .card-icon {
      font-size: 64px;
      margin-bottom: 20px;
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
        transform: scale(1.1);
        transition: transform 0.3s;
      }
    }
  }
}

@media (max-width: 768px) {
  .applications-content .applications-grid {
    grid-template-columns: 1fr;
  }
}
</style>

