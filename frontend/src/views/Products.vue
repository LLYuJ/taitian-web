<template>
  <div class="products-page">
    <div class="page-header">
      <div class="container">
        <h1>产品中心</h1>
        <p>提供精密机床、智能拧紧、节能空气压缩机等解决方案</p>
      </div>
    </div>

    <section class="products-content">
      <div class="container">
        <div class="products-list">
          <div class="product-item card">
            <div class="product-image">🔧</div>
            <div class="product-info">
              <h3>精密机床</h3>
              <p>高精度、高效率的精密机床设备，广泛应用于各类精密制造领域。</p>
            </div>
          </div>

          <div class="product-item card">
            <div class="product-image">⚙️</div>
            <div class="product-info">
              <h3>螺杆式空气压缩机</h3>
              <p>节能高效的空气压缩解决方案，满足各类工业用气需求。</p>
            </div>
          </div>

          <div class="product-item card">
            <div class="product-image">🔩</div>
            <div class="product-info">
              <h3>工业级扳手系列</h3>
              <p>专业的工业拧紧工具，高强度、高精度、高可靠性。</p>
            </div>
          </div>

          <div class="product-item card">
            <div class="product-image">🛠️</div>
            <div class="product-info">
              <h3>螺杆式空气压缩机主机</h3>
              <p>高性能压缩机主机，年产能达20万台。</p>
            </div>
          </div>

          <div class="product-item card">
            <div class="product-image">🔨</div>
            <div class="product-info">
              <h3>汽修工具系列</h3>
              <p>全方位的汽修工具解决方案，年产能100万台。</p>
            </div>
          </div>

          <div class="product-item card">
            <div class="product-image">💧</div>
            <div class="product-info">
              <h3>润滑设备</h3>
              <p>专业的润滑设备和解决方案。</p>
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
    align-items: center;
    gap: 25px;
    padding: 30px;
    background: white;

    .product-image {
      font-size: 64px;
      flex-shrink: 0;
    }

    .product-info {
      flex: 1;

      h3 {
        font-size: 22px;
        color: #333;
        margin-bottom: 12px;
      }

      p {
        font-size: 14px;
        color: #666;
        line-height: 1.6;
        margin: 0;
      }
    }
  }
}

@media (max-width: 768px) {
  .products-content .products-list {
    grid-template-columns: 1fr;
  }

  .product-item {
    flex-direction: column;
    text-align: center;
  }
}
</style>

