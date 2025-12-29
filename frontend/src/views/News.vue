<template>
  <div class="news-page">
    <div class="page-header">
      <div class="container">
        <h1>公司动态</h1>
        <p>了解泰田集团最新资讯</p>
      </div>
    </div>

    <section class="news-content">
      <div class="container">
        <div class="news-list">
          <div class="news-item card">
            <div class="news-date">
              <span class="day">11</span>
              <span class="month">2020-04</span>
            </div>
            <div class="news-info">
              <h3>2019年上海国际工业装配与传输技术展览会</h3>
              <p>2019年上海国际工业装配与传输技术展览会，将于2019年7月在上海举行...</p>
              <a href="#" class="read-more">阅读更多 →</a>
            </div>
          </div>

          <div class="news-item card">
            <div class="news-date">
              <span class="day">29</span>
              <span class="month">2018-10</span>
            </div>
            <div class="news-info">
              <h3>泰田集团喜获"浙江名牌产品"称号</h3>
              <p>"浙江名牌"荣誉是经区、市级质量监督管理部门严格审核通过...</p>
              <a href="#" class="read-more">阅读更多 →</a>
            </div>
          </div>

          <div class="news-item card">
            <div class="news-date">
              <span class="day">11</span>
              <span class="month">2020-04</span>
            </div>
            <div class="news-info">
              <h3>《冲击式气扳机》"浙江制造"团体标准评审会在我司召开</h3>
              <p>"浙江制造"是浙江省启动的将"浙江制造"打造成为具有严格认证...</p>
              <a href="#" class="read-more">阅读更多 →</a>
            </div>
          </div>

          <div class="news-item card">
            <div class="news-date">
              <span class="day">19</span>
              <span class="month">2018-10</span>
            </div>
            <div class="news-info">
              <h3>泰田集团通过浙江省省级企业研究院认定</h3>
              <p>省科技厅近日公布了2018年省级企业研究院认定名单，泰田集团...</p>
              <a href="#" class="read-more">阅读更多 →</a>
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

.news-content {
  padding: 80px 0;
  background: #f8f9fa;

  .news-list {
    max-width: 900px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 30px;
  }

  .news-item {
    display: flex;
    gap: 30px;
    padding: 30px;
    background: white;

    .news-date {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-width: 80px;
      padding: 15px;
      background: #2CB5BE;
      color: white;
      border-radius: 8px;

      .day {
        font-size: 32px;
        font-weight: 700;
        line-height: 1;
      }

      .month {
        font-size: 14px;
        margin-top: 5px;
      }
    }

    .news-info {
      flex: 1;

      h3 {
        font-size: 20px;
        color: #333;
        margin-bottom: 12px;
        transition: color 0.3s;

        &:hover {
          color: #2CB5BE;
        }
      }

      p {
        font-size: 14px;
        color: #666;
        line-height: 1.6;
        margin-bottom: 15px;
      }

      .read-more {
        color: #2CB5BE;
        text-decoration: none;
        font-size: 14px;
        font-weight: 500;
        transition: all 0.3s;

        &:hover {
          color: #1a8a91;
          transform: translateX(5px);
          display: inline-block;
        }
      }
    }
  }
}

@media (max-width: 768px) {
  .news-item {
    flex-direction: column;

    .news-date {
      min-width: auto;
      flex-direction: row !important;
      gap: 10px;
      justify-content: flex-start !important;
    }
  }
}
</style>

