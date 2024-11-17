<template>
  <div class="home-view relative flex flex-col items-center justify-center">
    <section class="relative z-10 flex flex-col justify-center items-center w-full space-y-6 text-center py-28">
      <div class="text-5xl my-1 typing-text">
        <span class="caveat-font text-gray-800">I want to... </span>
        <span class="caveat-font text-gray-800">{{ currentText }}</span>
      </div>
      
      <!-- Main header with goal-related message -->
      <header class="pb-6">
        <h1 class="text-6xl font-extrabold text-gray-800 leading-tight">
          Set Your Goals, Share Your Journey
        </h1>
        <p class="text-gray-500 mt-4 text-xl mx-auto w-3/4">
          Effortlessly manage your goals alongside loved ones. Set personalized targets, track progress in real-time, and stay motivated together as you turn your dreams into reality.
        </p>
      </header>

      <!-- Button for Unauthenticated Users -->
      <button
        v-if="!isAuthenticated"
        @click="goToSignUp"
        class="bg-gray-800 text-white py-4 px-10 rounded-full shadow-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out text-lg"
      >
        Join GoalBond Now!
      </button>

      <!-- Buttons for Authenticated Users -->
      <div v-if="isAuthenticated" class="flex space-x-6 mt-8">
        <button
          @click="goToGoals"
          class="bg-gray-800 text-white py-4 px-10 rounded-full shadow-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out text-lg"
        >
          Check Goals
        </button>
        <button
          @click="goToGroups"
          class="bg-gray-800 text-white py-4 px-10 rounded-full shadow-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out text-lg"
        >
          Check Groups
        </button>
      </div>
    </section>

    <div class="screenshot-placeholder flex justify-center items-center pb-28">
      <div class="relative w-5/12">
        <img 
          src="https://images.unsplash.com/photo-1553649033-3fbc8d0fa3cb?ixlib=rb-4.0.3" 
          alt="Screenshot of Goals Page" 
          class=" rounded-xl w-full h-auto" 
          style="mask-image: linear-gradient(to bottom, black 60%, transparent 100%);" 
        />
      </div>
    </div>

    <section class="bg-gray-100 overflow-hidden py-14 mx-20">
      <div class="flex justify-center items-center mx-auto">
        <!-- Step 1 -->
        <div class="flex flex-col items-center relative z-10 mx-4">
          <div class="bg-gray-800 text-white rounded-full w-12 h-12 flex items-center justify-center mb-2">
            1
          </div>
          <p class="text-lg font-semibold text-center">Create Account</p>
          <p class="text-gray-600 text-center">Sign up easily to get started with your goals.</p>
        </div>

        <!-- Line connecting Step 1 and Step 2 -->
        <div class="flex items-center">
          <div class="h-1 w-16 bg-gray-300"></div>
          <div class="w-0 h-0 border-t-8 border-b-8 border-l-8 border-transparent border-l-gray-300"></div>
        </div>
        <!-- Step 2 -->
        <div class="flex flex-col items-center relative z-10 mx-4">
          <div class="bg-gray-800 text-white rounded-full w-12 h-12 flex items-center justify-center mb-2">
            2
          </div>
          <p class="text-lg font-semibold text-center">Group Up</p>
          <p class="text-gray-600 text-center">(Optionally) Join or create groups to work together.</p>
        </div>

        <!-- Line connecting Step 2 and Step 3 -->
        <div class="flex items-center">
          <div class="h-1 w-16 bg-gray-300"></div>
          <div class="w-0 h-0 border-t-8 border-b-8 border-l-8 border-transparent border-l-gray-300"></div>
        </div>
        <!-- Step 3 -->
        <div class="flex flex-col items-center relative z-10 mx-4">
          <div class="bg-gray-800 text-white rounded-full w-12 h-12 flex items-center justify-center mb-2">
            3
          </div>
          <p class="text-lg font-semibold text-center">Set Your Goals</p>
          <p class="text-gray-600 text-center">Define your personal or group goals to stay focused.</p>
        </div>

        <!-- Line connecting Step 3 and Step 4 -->
        <div class="flex items-center">
          <div class="h-1 w-16 bg-gray-300"></div>
          <div class="w-0 h-0 border-t-8 border-b-8 border-l-8 border-transparent border-l-gray-300"></div>
        </div>
        <!-- Step 4 -->
        <div class="flex flex-col items-center relative z-10 mx-4">
          <div class="bg-gray-800 text-white rounded-full w-12 h-12 flex items-center justify-center mb-2">
            4
          </div>
          <p class="text-lg font-semibold text-center">Track Progress</p>
          <p class="text-gray-600 text-center">Monitor your progress and celebrate achievements.</p>
        </div>
      </div>
    </section>

    <section class="py-20 px-20">
      <h2 class="text-4xl font-bold text-gray-800 text-center my-14">What Our Users Say</h2>
      <div class="relative w-full max-w-8xl flex items-center justify-center mt-12 pb-16">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div
            v-for="(testimonial, index) in testimonials"
            :key="index"
            class="w-full mx-auto rounded-lg bg-white shadow-lg px-5 pt-5 pb-10 text-gray-800 transition-transform duration-300 transform hover:scale-105"
            style="max-width: 500px;"
          >
            <div class="w-full pt-1 pb-5">
              <div class="overflow-hidden rounded-full w-20 h-20 -mt-16 mx-auto shadow-lg">
                <img :src="testimonial.image" alt="" class="w-full h-full object-cover" />
              </div>
            </div>
            <div class="w-full mb-10 text-center">
              <div class="text-3xl text-indigo-500 text-left leading-tight h-3">“</div>
              <p class="text-sm text-gray-600 px-5">{{ testimonial.quote }}</p>
              <div class="text-3xl text-indigo-500 text-right leading-tight h-3 -mt-3">”</div>
            </div>
            <div class="w-full text-center">
              <p class="text-md text-indigo-500 font-bold">{{ testimonial.author }}</p>
              <p class="text-xs text-gray-500">@{{ testimonial.username }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>



  </div>
</template>



<script>
import { computed, ref, onMounted } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router'; 
export default {
  name: 'HomeView',
  components: {
  },
  setup() {
    const store = useStore();
    const router = useRouter();

    const isAuthenticated = computed(() => store.getters.isAuthenticated);
    const username = computed(() => store.getters.getUsername || '');

    const currentText = ref('');
    const texts = ref(['visit Paris', 'see a movie', 'eat sushi']);
    const currentIndex = ref(0);
    const typingSpeed = 100;
    const erasingSpeed = 50;
    const delayBetweenTexts = 1500;

    const testimonials = [
      {
        quote: "GoalBond helped me achieve my travel goals! I finally visited Paris!",
        author: "Sarah T.",
        image: "https://randomuser.me/api/portraits/women/15.jpg"
      },
      {
        quote: "The collaborative features made planning with friends so easy and fun!",
        author: "John D.",
        image: "https://randomuser.me/api/portraits/men/15.jpg"
      },
      {
        quote: "I was able to finally complete my bucket list thanks to GoalBond!",
        author: "Emily W.",
        image: "https://randomuser.me/api/portraits/women/16.jpg"
      },
      {
        quote: "GoalBond is a great tool for keeping track of goals and progress. I love it!",
        author: "David M.",
        image: "https://randomuser.me/api/portraits/men/16.jpg"
      }
    ];

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

    const currentSlide = ref(0);

    const nextSlide = () => {
      currentSlide.value = (currentSlide.value + 1) % slides.length;
    };

    const prevSlide = () => {
      currentSlide.value = (currentSlide.value - 1 + slides.length) % slides.length;
    };

    // Auto-advance slides every 5 seconds
    onMounted(() => {
      setInterval(nextSlide, 5000);
    });

    const goToSignUp = () => {
      router.push('/signup');
    };

    const goToGoals = () => {
      router.push('/goals');
    };

    const goToGroups = () => {
      router.push('/groups');
    };

    const typeText = () => {
      const fullText = texts.value[currentIndex.value];
      let charIndex = 0;

      const type = () => {
        if (charIndex < fullText.length) {
          currentText.value += fullText[charIndex];
          charIndex++;
          setTimeout(type, typingSpeed);
        } else {
          setTimeout(eraseText, delayBetweenTexts); // Pause before erasing
        }
      };

      type();
    };

    const eraseText = () => {
      const erase = () => {
        if (currentText.value.length > 0) {
          currentText.value = currentText.value.slice(0, -1);
          setTimeout(erase, erasingSpeed);
        } else {
          currentIndex.value = (currentIndex.value + 1) % texts.value.length; // Move to the next text
          typeText();
        }
      };

      erase();
    };

    // Start autoplay on mounted and stop on unmounted
    onMounted(typeText);

    return {
      isAuthenticated,
      username,
      goToSignUp,
      goToGoals,
      goToGroups,
      testimonials,
      currentText,
      slides,
      currentSlide,
      nextSlide,
      prevSlide,
    };
  },
};
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400..700&display=swap');

.caveat-font {
  font-family: "Caveat", cursive;
  font-optical-sizing: auto;
  font-weight: 100;
  font-style: normal;
}

.home-view {
  font-family: 'Inter', sans-serif;
}

.feature-highlights {
  background-color: #f9f9f9; /* Light background for contrast */
  padding: 40px 0; /* Padding for top and bottom */
  border-radius: 10px; /* Rounded corners */
}

.feature-card {
  transition: transform 0.3s;
}

.feature-card:hover {
  transform: translateY(-5px); /* Slight lift effect on hover */
}

</style>
