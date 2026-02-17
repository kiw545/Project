from pyscript import document, when  # type:ignore
from js import window  # type:ignore

class Fruit:
    def __init__(self):
        self.sound_text = ""
        self.display_text = ""

    def speak_benefit(self):
        if self.sound_text:
            utterance = window.SpeechSynthesisUtterance.new(self.sound_text)

            utterance.lang = "th-TH"

            # 🎀 เสียงน่ารัก
            utterance.pitch = 1.6
            utterance.rate = 1.1
            utterance.volume = 1

            voices = window.speechSynthesis.getVoices()

            for voice in voices:
                if "th" in voice.lang.lower():
                    utterance.voice = voice
                    break

            window.speechSynthesis.cancel()
            window.speechSynthesis.speak(utterance)

        return self.display_text

class Apple(Fruit):
    def __init__(self):
        self.sound_text = "กูคือแอปเปิ้ลกินซะมีไฟเบอร์สูง ช่วยในการขับถ่าย และดีต่อหัวใจ"
        self.display_text = "แอปเปิ้ลช่วยบำรุงหัวใจและระบบขับถ่าย"


class Banana(Fruit):
    def __init__(self):
        self.sound_text = "กูคือกล้วยให้พลังงานสูง และมีโพแทสเซียม ช่วยลดอาการตะคริว"
        self.display_text = "กล้วยช่วยให้พลังงานและลดตะคริว"


class Mango(Fruit):
    def __init__(self):
        self.sound_text = "กูคือมะม่วงมีวิตามินเอสูง ช่วยบำรุงสายตา และเสริมภูมิคุ้มกัน"
        self.display_text = "มะม่วงช่วยบำรุงสายตาและภูมิคุ้มกัน"


class Watermelon(Fruit):
    def __init__(self):
        self.sound_text = "กูคือแตงโมมีน้ำมาก ช่วยให้ร่างกายสดชื่น และป้องกันการขาดน้ำ"
        self.display_text = "แตงโมช่วยให้สดชื่นและเติมน้ำให้ร่างกาย"


@when("click", "#btn_sound")
def play_sound(event):
    choice = document.getElementById("fruit_selector").value
    fruit = None

    if choice == "apple":
        fruit = Apple()
    elif choice == "banana":
        fruit = Banana()
    elif choice == "mango":
        fruit = Mango()
    elif choice == "watermelon":
        fruit = Watermelon()

    if fruit:
        text = fruit.speak_benefit()
        document.getElementById("output").innerText = text
