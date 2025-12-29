<template>
  <div class="main-layout">
    <header class="header">
      <div class="container header-content">
        <div class="logo">
          <h1>泰田集团</h1>
        </div>
        <nav class="nav">
          <router-link to="/" class="nav-item">首页</router-link>
          <router-link to="/about" class="nav-item">关于泰田</router-link>
          <router-link to="/products" class="nav-item">产品中心</router-link>
          <router-link to="/applications" class="nav-item">行业应用</router-link>
          <router-link to="/news" class="nav-item">公司动态</router-link>
          <router-link to="/contact" class="nav-item">联系我们</router-link>
        </nav>
        <div class="header-actions">
          <router-link to="/admin" class="admin-link">管理后台</router-link>
        </div>
      </div>
    </header>

    <main class="main-content">
      <router-view />
    </main>

    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-section">
            <h3>联系我们</h3>
            <p>服务热线：400-826-1128</p>
            <p>公司邮箱：sales@chinatuta.com</p>
            <p>公司地址：浙江省台州市椒江区海韵路528号</p>
          </div>
          <div class="footer-section">
            <h3>快速链接</h3>
            <router-link to="/about">关于我们</router-link>
            <router-link to="/products">产品中心</router-link>
            <router-link to="/news">公司动态</router-link>
            <router-link to="/contact">联系我们</router-link>
          </div>
          <div class="footer-section">
            <h3>关注我们</h3>
            <p>微信公众号</p>
          </div>
        </div>
        <div class="footer-bottom">
          <p>COPYRIGHT © 泰田集团股份有限公司 版权所有 ALL RIGHTS RESERVED</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
</script>

<style lang="scss" scoped>
.main-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.header {
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 1000;

  .header-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 80px;
  }

  .logo {
    h1 {
      color: #2CB5BE;
      font-size: 28px;
      font-weight: 700;
      margin: 0;
    }
  }

  .nav {
    display: flex;
    gap: 40px;

    .nav-item {
      color: #333;
      text-decoration: none;
      font-size: 16px;
      font-weight: 500;
      position: relative;
      transition: color 0.3s;

      &:hover, &.router-link-active {
        color: #2CB5BE;
      }

      &.router-link-active::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        right: 0;
        height: 3px;
        background: #2CB5BE;
      }
    }
  }

  .header-actions {
    .admin-link {
      color: #666;
      text-decoration: none;
      font-size: 14px;
      
      &:hover {
        color: #2CB5BE;
      }
    }
  }
}

.main-content {
  flex: 1;
}

.footer {
  background: #1a1a1a;
  color: white;
  padding: 60px 0 20px;
  margin-top: 80px;

  .footer-content {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 60px;
    margin-bottom: 40px;
  }

  .footer-section {
    h3 {
      color: #2CB5BE;
      font-size: 18px;
      margin-bottom: 20px;
    }

    p, a {
      color: #ccc;
      margin: 10px 0;
      font-size: 14px;
      text-decoration: none;
      display: block;

      &:hover {
        color: #2CB5BE;
      }
    }
  }

  .footer-bottom {
    border-top: 1px solid #333;
    padding-top: 20px;
    text-align: center;

    p {
      color: #666;
      font-size: 14px;
    }
  }
}

@media (max-width: 768px) {
  .header {
    .header-content {
      flex-wrap: wrap;
      height: auto;
      padding: 15px 0;
    }

    .nav {
      width: 100%;
      flex-wrap: wrap;
      gap: 15px;
    }
  }

  .footer {
    .footer-content {
      grid-template-columns: 1fr;
      gap: 30px;
    }
  }
}
</style>

