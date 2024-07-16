import random
import re

class RuleBot:
  ### Potential Negative Responses
  negative_responses = ("no","nope","nah","naw","not a chance", "sorry")
  ### Exit converstion Keywords
  exit_commands = ("quit","pause","exit","goodbye","bye","later")
  ### Random starter question
  random_questions = (
      "why are you here?",
      "Are there many humans like you?",
      "What do you consume for substance?",
      "Is there intelliget life on this planet?",
      "Does Earth have a leader?",
      "What planets have you visited? ",
      "What technology do you have on this planet? "
  )

  def __init__(self):
    self.allienabble = {
                         'describe_planet_intent': r'.*\s* your planet.*',
                         'answer_why_intent': r'why\sare.*',
                         'about_intellipat': r'.*\s*intellipaat',
                         'about_session': r'.*\s*session'
                        # 'describe_planet_intent': r'.*\s+your\s+planet.*',
                        # 'answer_why_intent': r'why\s+are.*',
                        # 'about_intellipat': r'.*\s+intellipaat.*'
                        }
  def greet(self):
    self.name = input("What is your name?\n")
    will_help = input(f"Hi {self.name}, I am Rule-Bot. will you help me learn your planet?\n")
    if will_help in self.negative_responses:
      print("Ok, have a nice day!")
      return
    self.chat()
  def make_exit(self,reply):
    for command in self.exit_commands:
      if reply == command:
        print("Okay, have a nice day!")
        return True
  def chat(self):
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
      reply = input(self.match_reply(reply))

  def match_reply(self,reply):
    for key , value in self.allienabble.items():
      intent = key
      regex_pattern = value
      #below comented code need to be checked
      #found_match = re.match(regex_pattern,reply)
      found_match = re.search(reply,regex_pattern)
      if found_match and intent == 'describe_planet_intent':
        return self.describe_planet_intent()
      elif found_match and intent == 'answer_why_intent':
        return self.answer_why_intent()
      elif found_match and intent == 'about_intellipat':
        return self.about_intellipat()
      elif found_match and intent == 'about_session':
        return self.about_session()
    if not found_match:
      return self.no_match_intent()

  def describe_planet_intent(self):
    responses = ("My planet is a utopia of diverse organism and species.\n",
                  "I am from opidipus , the capital of the wayward Galaxies.\n")
    return random.choice(responses)

  def answer_why_intent(self):
    responses = ("I come in peace\n","I am here to collect data on your planet and its inhabitats\n",
                  "I heard the coffee is good\n")
    return random.choice(responses)

  def about_intellipat(self):
    responses = ("intellipaat is a world's largest professional educatinal company\n",
                  "intellipaat will make you learn concepts in tha way never ",
                  "Intellipat is where you carrer ad skill grows\n")
    return random.choice(responses)
  
  def about_session(self):
    responses = ('Session is on 14th Aug 2022\n','session was cool!!')
    return random.choice(responses)
  
  def no_match_intent(self):
    responses = (
        "Please tell me more. \n", "Tell me more!\n", "I see. Can you elaborate?\n",
        "Interesting. Can you tell me more?\n", "I see. How do you think?\n",
        "Why?\n","How do you think I feel when you say that?\n")
    return random.choice(responses)

AlienBot = RuleBot()
AlienBot.greet()

