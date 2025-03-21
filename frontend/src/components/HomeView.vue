<template>
  <div class="home-view relative flex flex-col items-center justify-center">
    <section class="flex items-center">
      <div class="flex items-start w-1/2 ml-64">
        <section class="relative z-10 flex flex-col justify-start items-start w-full space-y-6 text-left py-28">
          <div class="text-5xl my-1 typing-text">
            <span class="caveat-font text-gray-800">I want to... </span>
            <span class="caveat-font text-gray-800">{{ currentText }}</span>
          </div>

          <!-- Main header with goal-related message -->
          <header class="pb-6">
            <h1 class="text-5xl font-extrabold text-gray-800 leading-tight">
              Set Your Goals, Share Your Journey
            </h1>
            <p class="text-gray-500 mt-4 text-xl w-3/4">
              Manage your goals with loved ones. Set targets, track progress, and stay motivated together.
            </p>
          </header>

          <!-- Button for Unauthenticated Users -->
          <button
            v-if="!isAuthenticated"
            @click="goToSignUp"
            class="border-2 border-[#B03052] text-[#B03052] font-bold py-4 px-10 rounded-full shadow-lg hover:bg-[#B03052] hover:text-white transition-all duration-300 ease-in-out text-lg"
          >
            Join GoalBond Now!
          </button>

          <!-- Buttons for Authenticated Users -->
          <div v-if="isAuthenticated" class="flex space-x-6 mt-8">
            <button
              @click="goToGoals"
              class="bg-[#B03052] text-white py-4 px-10 rounded-full shadow-lg hover:bg-[#3D0301] transition-all duration-300 ease-in-out text-lg"
            >
              My Goals
            </button>
            <button
              @click="goToGroups"
              class="bg-[#B03052] text-white py-4 px-10 rounded-full shadow-lg hover:bg-[#3D0301] transition-all duration-300 ease-in-out text-lg"
            >
              My Account
            </button>
          </div>
        </section>
      </div>

      <div class="flex items-left w-1/2 mr-64 mt-10">       
        <div class="screenshot-placeholder flex justify-center items-center pb-28">
          <div class="relative w-2/3 transform">
            <svg width="500px" height="400px" viewBox="0 0 36 36" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="iconify iconify--twemoji" preserveAspectRatio="xMidYMid meet">
              <path fill="#B03052" d="M27 8a6.98 6.98 0 0 0-2.015.298c.005-.1.015-.197.015-.298a5.998 5.998 0 0 0-11.785-1.573A5.974 5.974 0 0 0 11 6a6 6 0 1 0 0 12a5.998 5.998 0 0 0 5.785-4.428A5.975 5.975 0 0 0 19 14c.375 0 .74-.039 1.096-.104c-.058.36-.096.727-.096 1.104c0 3.865 3.135 7 7 7s7-3.135 7-7a7 7 0 0 0-7-7z"/>
              <path fill="#D76C82" d="M31 22c-.467 0-.91.085-1.339.204c.216-.526.339-1.1.339-1.704a4.5 4.5 0 0 0-4.5-4.5a4.459 4.459 0 0 0-2.701.921A6.497 6.497 0 0 0 16.5 12a6.497 6.497 0 0 0-6.131 4.357A8 8 0 1 0 8 32h23c2.762 0 5-2.238 5-5s-2.238-5-5-5z"/>
            </svg>
          </div>
        </div>
      </div>
    </section>

    <section class="overflow-hidden py-14 mx-20">
      <div class="flex justify-center items-center mx-auto">
        <div class="flex flex-col items-center relative mx-4">
          <div class="bg-[#B03052] text-white rounded-full w-12 h-12 flex items-center justify-center mb-2">
            1
          </div>
          <p class="text-lg font-semibold text-center">Create Account</p>
          <p class="text-gray-600 text-center">Sign up today to get started with your goals!</p>
        </div>

        <div class="flex items-center">
          <div class="h-1 w-16 bg-[#3D0301]"></div>
          <div class="w-0 h-0 border-t-8 border-b-8 border-l-8 border-transparent border-l-[#3D0301]"></div>
        </div>
        <div class="flex flex-col items-center relative mx-4">
          <div class="bg-[#B03052] text-white rounded-full w-12 h-12 flex items-center justify-center mb-2">
            2
          </div>
          <p class="text-lg font-semibold text-center">Group Up</p>
          <p class="text-gray-600 text-center">Join or create groups to work together.</p>
        </div>

        <div class="flex items-center">
          <div class="h-1 w-16 bg-[#3D0301]"></div>
          <div class="w-0 h-0 border-t-8 border-b-8 border-l-8 border-transparent border-l-[#3D0301]"></div>
        </div>
        <div class="flex flex-col items-center relative mx-4">
          <div class="bg-[#B03052] text-white rounded-full w-12 h-12 flex items-center justify-center mb-2">
            3
          </div>
          <p class="text-lg font-semibold text-center">Set Your Goals</p>
          <p class="text-gray-600 text-center">Define your personal or group goals to stay focused.</p>
        </div>

        <div class="flex items-center">
          <div class="h-1 w-16 bg-[#3D0301]"></div>
          <div class="w-0 h-0 border-t-8 border-b-8 border-l-8 border-transparent border-l-[#3D0301]"></div>
        </div>
        <div class="flex flex-col items-center relative mx-4">
          <div class="bg-[#B03052] text-white rounded-full w-12 h-12 flex items-center justify-center mb-2">
            4
          </div>
          <p class="text-lg font-semibold text-center">Track Progress</p>
          <p class="text-gray-600 text-center">Monitor your progress and celebrate achievements.</p>
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

    const goToSignUp = () => {
      router.push('/signup');
    };

    const goToGoals = () => {
      router.push('/goals');
    };

    const goToGroups = () => {
      router.push('/account');
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

    onMounted(typeText);

    return {
      isAuthenticated,
      username,
      goToSignUp,
      goToGoals,
      goToGroups,
      currentText
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
  background-color: #f9f9f9; 
  padding: 40px 0; 
  border-radius: 10px; 
}

.feature-card {
  transition: transform 0.3s;
}

.feature-card:hover {
  transform: translateY(-5px); 
}

</style>
