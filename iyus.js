// 播放语音的dom
let audio = ref<HTMLAudioElement>();
// 播放语音的状态
let playStauts = ref<boolean>(false);

/**
 * @description: 控制 读题语音播放
 * @return {*}
 * @author: jlx
 */
const handleVoice = () => {
  audio.value = new Audio(
    `http://tts.youdao.com/fanyivoice?word=${problem.value.brief}&le=zh&keyfrom=speaker-target`
  );
  // 如果 语音正在播放中
  if (playStauts.value) {
    audio.value?.pause();
    playStauts.value = false;
  } else {
    // 语音没有播放，打开播放
    audio.value?.play();
    playStauts.value = true;
  }
};
