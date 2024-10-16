<template>
  <div class="carousel-container w-full max-w-6xl mx-auto py-20">
    <Carousel 
      :items-to-show="1" 
      :wrap-around="true" 
      :transition="500"
      :autoplay="3000"
      :pause-autoplay-on-hover="true"
    >
      <Slide v-for="(slide, index) in slides" :key="index">
        <div class="carousel__item">
          <img :src="slide.image" :alt="slide.alt" class="carousel-image rounded-xl">
          <p class="carousel-text">{{ slide.text }}</p>
        </div>
      </Slide>

      <template #addons>
        <Pagination />
      </template>
    </Carousel>
  </div>
</template>

<script>
import { Carousel, Slide, Pagination } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'

export default {
  name: 'CarouselView',
  components: {
    Carousel,
    Slide,
    Pagination,
  },
  setup() {
    const slides = [
      {
        image: "https://images.unsplash.com/photo-1725582205921-7d681ebca2a7?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        alt: "Habit Tracker",
        text: "Build habits and achieve goals"
      },
      {
        image: "https://images.unsplash.com/photo-1502444330042-d1a1ddf9bb5b?q=80&w=2073&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        alt: "Group Chat",
        text: "Connect with friends and join groups"
      },
      {
        image: "https://images.unsplash.com/photo-1536010447069-d2c8af80c584?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        alt: "Progress Tracker",
        text: "Track your progress and stay motivated"
      }
    ];

    return {
      slides,
    };
  },
};
</script>

<style scoped>
.carousel-container {
  position: relative;
}

.carousel__item {
  position: relative;
  height: 600px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.carousel-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.carousel-text {
  position: absolute;
  bottom: 40px;
  left: 40px;
  background-color: rgba(255, 255, 255, 0.8);
  padding: 15px;
  border-radius: 8px;
  font-size: 1.75rem;
  font-weight: bold;
  color: #333;
  left: auto;
  right:auto;
}

:deep(.carousel__slide) {
  padding: 0;
}

:deep(.carousel__prev),
:deep(.carousel__next) {
  background-color: rgba(255, 255, 255, 0.7);
  border-radius: 50%;
  width: 50px;
  height: 50px;
}

:deep(.carousel__pagination) {
  padding-top: 20px;
}
</style>
