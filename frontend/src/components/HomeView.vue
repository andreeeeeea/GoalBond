<template>
  <div class="home-view bg-[#FEFEFD]">
    <!-- Hero Section -->
    <section class="relative min-h-screen flex items-center justify-center overflow-hidden">
      <!-- Animated Background -->
      <div class="absolute inset-0 z-0">
        <div class="absolute top-20 left-10 w-72 h-72 bg-[#D76C82] rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob"></div>
        <div class="absolute top-40 right-20 w-72 h-72 bg-[#B03052] rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-2000"></div>
        <div class="absolute -bottom-8 left-40 w-72 h-72 bg-[#D76C82] rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-4000"></div>
      </div>

      <div class="container mx-auto px-6 relative z-10">
        <div class="flex flex-col lg:flex-row items-center justify-between">
          <!-- Left Content -->
          <div class="lg:w-1/2 mb-10 lg:mb-0">
            <div class="mb-8">
              <span class="text-[#B03052] font-semibold text-lg">Welcome to GoalBond</span>
            </div>
            
            <!-- Animated Typing Text -->
            <h1 class="text-5xl lg:text-7xl font-bold text-gray-800 mb-6 leading-tight">
              Turn Dreams Into
              <span class="block text-[#B03052] mt-2">
                <span class="typing-text">{{ currentText }}</span>
                <span class="cursor">|</span>
              </span>
            </h1>
            
            <p class="text-xl text-gray-600 mb-8 leading-relaxed">
              Join thousands achieving their goals together. Track progress, stay motivated, and celebrate victories with friends and family.
            </p>

            <!-- CTA Buttons -->
            <div class="flex flex-col sm:flex-row gap-4">
              <button
                v-if="!isAuthenticated"
                @click="goToSignUp"
                class="px-8 py-4 bg-[#B03052] text-white font-bold rounded-xl hover:bg-[#8B2440] transform hover:scale-105 transition-all duration-300 shadow-lg hover:shadow-xl"
              >
                Start Your Journey Free
              </button>
              <button
                v-if="!isAuthenticated"
                @click="$router.push('/login')"
                class="px-8 py-4 bg-white text-[#B03052] font-bold rounded-xl border-2 border-[#B03052] hover:bg-[#B03052] hover:text-white transform hover:scale-105 transition-all duration-300"
              >
                Sign In
              </button>
              
              <!-- Authenticated User Buttons -->
              <button
                v-if="isAuthenticated"
                @click="goToGoals"
                class="px-8 py-4 bg-[#B03052] text-white font-bold rounded-xl hover:bg-[#8B2440] transform hover:scale-105 transition-all duration-300 shadow-lg hover:shadow-xl"
              >
                View My Goals
              </button>
              <button
                v-if="isAuthenticated"
                @click="goToGroups"
                class="px-8 py-4 bg-white text-[#B03052] font-bold rounded-xl border-2 border-[#B03052] hover:bg-[#B03052] hover:text-white transform hover:scale-105 transition-all duration-300"
              >
                My Account
              </button>
            </div>

          </div>

          <!-- Right Visual -->
          <div class="lg:w-1/2 relative">
            <div class="relative w-full max-w-lg mx-auto">
              <!-- Floating Cards Animation -->
              <div class="absolute inset-0 flex items-center justify-center">
                <div class="relative w-full h-[500px]">
                  <!-- Goal Card 1 -->
                  <div class="absolute top-0 right-10 bg-white rounded-xl shadow-xl p-6 w-64 transform rotate-6 hover:rotate-0 transition-transform duration-300 animate-float">
                    <div class="flex items-center justify-between mb-3">
                      <span class="text-sm font-semibold text-[#B03052]">Fitness Goal</span>
                    </div>
                    <h4 class="font-bold text-gray-800 mb-2">Run a Marathon</h4>
                    <div class="w-full bg-gray-200 rounded-full h-2">
                      <div class="bg-gradient-to-r from-[#B03052] to-[#D76C82] h-2 rounded-full" style="width: 75%"></div>
                    </div>
                    <p class="text-sm text-gray-600 mt-2">75% Complete</p>
                  </div>

                  <!-- Goal Card 2 -->
                  <div class="absolute top-32 left-0 bg-white rounded-xl shadow-xl p-6 w-64 transform -rotate-6 hover:rotate-0 transition-transform duration-300 animate-float animation-delay-2000">
                    <div class="flex items-center justify-between mb-3">
                      <span class="text-sm font-semibold text-[#B03052]">Learning Goal</span>
                    </div>
                    <h4 class="font-bold text-gray-800 mb-2">Learn Spanish</h4>
                    <div class="flex -space-x-2 mb-2">
                      <div class="w-8 h-8 bg-[#D76C82] rounded-full border-2 border-white flex items-center justify-center text-white text-xs">A</div>
                      <div class="w-8 h-8 bg-[#B03052] rounded-full border-2 border-white flex items-center justify-center text-white text-xs">B</div>
                      <div class="w-8 h-8 bg-[#8B2440] rounded-full border-2 border-white flex items-center justify-center text-white text-xs">+3</div>
                    </div>
                    <p class="text-sm text-gray-600">5 members working together</p>
                  </div>

                  <!-- Goal Card 3 -->
                  <div class="absolute bottom-10 right-5 bg-white rounded-xl shadow-xl p-6 w-64 transform rotate-3 hover:rotate-0 transition-transform duration-300 animate-float animation-delay-4000">
                    <div class="flex items-center justify-between mb-3">
                      <span class="text-sm font-semibold text-[#B03052]">Creative Goal</span>
                    </div>
                    <h4 class="font-bold text-gray-800 mb-2">Write a Novel</h4>
                    <div class="flex items-center gap-2 text-sm text-gray-600">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                      <span>2 days until next milestone</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Wave Transition -->
    <div class="relative">
      <svg class="absolute top-0 w-full h-24 -mt-5 sm:-mt-10 sm:h-32" preserveAspectRatio="none" viewBox="0 0 1440 100">
        <path fill="#FEFEFD" d="M0,0 C480,100 960,100 1440,0 L1440,100 L0,100 Z"></path>
      </svg>
    </div>

    <!-- Features Section -->
    <section class="py-20 bg-white relative">
      <div class="container mx-auto px-6">
        <div class="text-center mb-16">
          <h2 class="text-4xl font-bold text-gray-800 mb-4">Everything You Need to Succeed</h2>
          <p class="text-xl text-gray-600">Powerful features to help you achieve your dreams</p>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
          <!-- Feature 1 -->
          <div class="group hover:transform hover:scale-105 transition-all duration-300">
            <div class="bg-gradient-to-br from-[#B03052] to-[#D76C82] rounded-2xl p-8 text-white h-full">
              <div class="w-16 h-16 bg-white/20 rounded-xl flex items-center justify-center mb-6">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <h3 class="text-2xl font-bold mb-3">Track Progress</h3>
              <p class="opacity-90">Visual progress bars and milestones keep you motivated every step of the way.</p>
            </div>
          </div>

          <!-- Feature 2 -->
          <div class="group hover:transform hover:scale-105 transition-all duration-300">
            <div class="bg-white border-2 border-[#D76C82] rounded-2xl p-8 h-full">
              <div class="w-16 h-16 bg-[#D76C82]/10 rounded-xl flex items-center justify-center mb-6">
                <svg class="w-8 h-8 text-[#B03052]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
              </div>
              <h3 class="text-2xl font-bold mb-3 text-gray-800">Group Goals</h3>
              <p class="text-gray-600">Work together with friends and family. Share victories and support each other.</p>
            </div>
          </div>

          <!-- Feature 3 -->
          <div class="group hover:transform hover:scale-105 transition-all duration-300">
            <div class="bg-gradient-to-br from-[#D76C82] to-[#B03052] rounded-2xl p-8 text-white h-full">
              <div class="w-16 h-16 bg-white/20 rounded-xl flex items-center justify-center mb-6">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
                </svg>
              </div>
              <h3 class="text-2xl font-bold mb-3">Smart Categories</h3>
              <p class="opacity-90">Organize goals by categories like Fitness, Coding, Travel, and more.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- How It Works Section -->
    <section class="py-20 bg-gray-50">
      <div class="container mx-auto px-6">
        <div class="text-center mb-16">
          <h2 class="text-4xl font-bold text-gray-800 mb-4">How GoalBond Works</h2>
          <p class="text-xl text-gray-600">Your journey to success in four simple steps</p>
        </div>

        <div class="relative max-w-5xl mx-auto">
          <div class="grid md:grid-cols-4 gap-8 relative">
            <!-- Step 1 -->
            <div class="text-center relative group">
              <div class="bg-gradient-to-br from-[#B03052] to-[#D76C82] rounded-full w-20 h-20 flex items-center justify-center mx-auto mb-6 shadow-lg transform group-hover:scale-110 transition-transform duration-300">
                <span class="text-2xl font-bold text-white">1</span>
              </div>
              <!-- Curved connection to next step -->
              <div class="hidden md:block absolute top-10 left-1/2 w-full h-20">
                <svg class="w-full h-full" viewBox="0 0 200 80" preserveAspectRatio="none">
                  <path d="M 40 40 Q 100 20, 160 40" stroke="url(#gradient1)" stroke-width="2" fill="none" stroke-dasharray="5,5" opacity="0.3"/>
                  <defs>
                    <linearGradient id="gradient1" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" style="stop-color:#B03052" />
                      <stop offset="100%" style="stop-color:#D76C82" />
                    </linearGradient>
                  </defs>
                </svg>
              </div>
              <h3 class="text-xl font-bold mb-3 text-gray-800">Sign Up</h3>
              <p class="text-gray-600">Create your free account in seconds</p>
            </div>

            <!-- Step 2 -->
            <div class="text-center relative group">
              <div class="bg-gradient-to-br from-[#D76C82] to-[#B03052] rounded-full w-20 h-20 flex items-center justify-center mx-auto mb-6 shadow-lg transform group-hover:scale-110 transition-transform duration-300">
                <span class="text-2xl font-bold text-white">2</span>
              </div>
              <!-- Curved connection to next step -->
              <div class="hidden md:block absolute top-10 left-1/2 w-full h-20">
                <svg class="w-full h-full" viewBox="0 0 200 80" preserveAspectRatio="none">
                  <path d="M 40 40 Q 100 60, 160 40" stroke="url(#gradient2)" stroke-width="2" fill="none" stroke-dasharray="5,5" opacity="0.3"/>
                  <defs>
                    <linearGradient id="gradient2" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" style="stop-color:#D76C82" />
                      <stop offset="100%" style="stop-color:#B03052" />
                    </linearGradient>
                  </defs>
                </svg>
              </div>
              <h3 class="text-xl font-bold mb-3 text-gray-800">Set Goals</h3>
              <p class="text-gray-600">Define what you want to achieve</p>
            </div>

            <!-- Step 3 -->
            <div class="text-center relative group">
              <div class="bg-gradient-to-br from-[#B03052] to-[#D76C82] rounded-full w-20 h-20 flex items-center justify-center mx-auto mb-6 shadow-lg transform group-hover:scale-110 transition-transform duration-300">
                <span class="text-2xl font-bold text-white">3</span>
              </div>
              <!-- Curved connection to next step -->
              <div class="hidden md:block absolute top-10 left-1/2 w-full h-20">
                <svg class="w-full h-full" viewBox="0 0 200 80" preserveAspectRatio="none">
                  <path d="M 40 40 Q 100 20, 160 40" stroke="url(#gradient3)" stroke-width="2" fill="none" stroke-dasharray="5,5" opacity="0.3"/>
                  <defs>
                    <linearGradient id="gradient3" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" style="stop-color:#B03052" />
                      <stop offset="100%" style="stop-color:#D76C82" />
                    </linearGradient>
                  </defs>
                </svg>
              </div>
              <h3 class="text-xl font-bold mb-3 text-gray-800">Track Progress</h3>
              <p class="text-gray-600">Update your progress regularly</p>
            </div>

            <!-- Step 4 -->
            <div class="text-center relative group">
              <div class="bg-gradient-to-br from-[#D76C82] to-[#8B2440] rounded-full w-20 h-20 flex items-center justify-center mx-auto mb-6 shadow-lg transform group-hover:scale-110 transition-transform duration-300">
                <span class="text-2xl font-bold text-white">4</span>
              </div>
              <h3 class="text-xl font-bold mb-3 text-gray-800">Celebrate</h3>
              <p class="text-gray-600">Achieve your goals and set new ones</p>
            </div>
          </div>
        </div>
      </div>
    </section>


    <section class="pt-20 pb-0 bg-gradient-to-r from-[#B03052] to-[#D76C82] relative">
      <div class="container mx-auto px-6 text-center pb-20">
        <h2 class="text-4xl font-bold text-white mb-6">Ready to Achieve Your Goals?</h2>
        <p class="text-xl text-white/90 mb-8 max-w-2xl mx-auto">
          Join thousands of motivated individuals and start your journey to success today. It's free to get started!
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <button
            v-if="!isAuthenticated"
            @click="goToSignUp"
            class="px-8 py-4 bg-white text-[#B03052] font-bold rounded-xl hover:bg-gray-100 transform hover:scale-105 transition-all duration-300 shadow-lg"
          >
            Get Started For Free
          </button>
          
          <button
            v-if="isAuthenticated"
            @click="goToGoals"
            class="px-8 py-4 bg-white text-[#B03052] font-bold rounded-xl hover:bg-gray-100 transform hover:scale-105 transition-all duration-300 shadow-lg"
          >
            Go to Dashboard
          </button>
        </div>
      </div>
      <svg class="block w-full h-16" preserveAspectRatio="none" viewBox="0 0 1440 54">
        <path fill="#FEFEFD" d="M0 22L60 16.7C120 11 240 1.00001 360 0.700012C480 1.00001 600 11 720 21.2C840 31 960 41 1080 38.8C1200 37 1320 23 1380 16L1440 9V54H1380C1320 54 1200 54 1080 54C960 54 840 54 720 54C600 54 480 54 360 54C240 54 120 54 60 54H0V22Z"></path>
      </svg>
    </section>
  </div>
</template>

<script>
import { computed, ref, onMounted } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router'; 

export default {
  name: 'HomeView',
  setup() {
    const store = useStore();
    const router = useRouter();

    const isAuthenticated = computed(() => store.getters.isAuthenticated);
    const username = computed(() => store.getters.getUsername || '');

    const currentText = ref('');
    const texts = ref(['Achievements', 'Reality', 'Success', 'Habits', 'Progress']);
    const currentIndex = ref(0);
    const typingSpeed = 150;
    const erasingSpeed = 100;
    const delayBetweenTexts = 2000;

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
          setTimeout(eraseText, delayBetweenTexts);
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
          currentIndex.value = (currentIndex.value + 1) % texts.value.length;
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
.home-view {
  font-family: 'Inter', sans-serif;
}

/* Cursor animation */
.cursor {
  display: inline-block;
  animation: blink 1s infinite;
}

@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}

/* Blob animation */
@keyframes blob {
  0% {
    transform: translate(0px, 0px) scale(1);
  }
  33% {
    transform: translate(30px, -50px) scale(1.1);
  }
  66% {
    transform: translate(-20px, 20px) scale(0.9);
  }
  100% {
    transform: translate(0px, 0px) scale(1);
  }
}

.animate-blob {
  animation: blob 7s infinite;
}

.animation-delay-2000 {
  animation-delay: 2s;
}

.animation-delay-4000 {
  animation-delay: 4s;
}

/* Float animation */
@keyframes float {
  0% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-20px);
  }
  100% {
    transform: translateY(0px);
  }
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}
</style>