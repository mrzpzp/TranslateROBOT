#TranslateROBOT v2.9 by MrZpzp

import time
import praw
import os
import language_code_list
from googletrans import Translator
from prawcore.exceptions import Forbidden


def login():
    print("Logging in...")
    #Fill here
    reddit = praw.Reddit(client_id="my client id",
                         client_secret="my client secret",
                         user_agent="my user agent",
                         username="username",
                         password="password",
                        )
    print("Logged in!")

    return reddit


def reply(p_type, to_input):
  print("Related words found in " +
                        p_type.id)
                
  lang_code =  p_type.body  
  lang_code_a = lang_code.replace("u/translaterobot", "")
  lang_code_f = lang_code_a.replace(" ", "")
            
  if (lang_code_f in language_code_list.codes):         
    print("Using API")
    input = to_input

    if len(input) >= 3000:
 
      if lang_code_f == "tr":
        print("More than 3000 characters.Passed.")
        p_type.reply("*3000'den fazla karakter olduğu için bunu çeviremiyorum.Özür dilerim.* "  + "\n\n" + "^(Ben bir botum ve bu eylem otomatik olarak gerçekleştirildi.)" + "\n\n" + "[INFO](https://www.reddit.com/user/translaterobot/comments/pq1pdf/helloooo_i_am_translaterobot_en/)")
      else:
        print("More than 3000 characters.Passed.")
        p_type.reply("*I can't translate this becasue it has more than 3000 characters.Sorry about that.* "  + "\n\n" + "^(I am a bot and this action was performed automatically.)" + "\n\n" + "[INFO](https://www.reddit.com/user/translaterobot/comments/pq1pdf/helloooo_i_am_translaterobot_en/)")
                  
    else:
      translator = Translator()
      output = translator.translate(input, dest=lang_code_f)
      text_output_a = output.text
      text_output_b = text_output_a.replace("** ", "**")
      text_output_c = text_output_b.replace(" **", "**")
      text_output = text_output_c


      if lang_code_f == "tr":
        p_type.reply("*Beep boop, işte çevirin:* " + "\n\n" + text_output + " \n\n " + "^(Ben bir botum ve bu eylem otomatik olarak gerçekleştirildi.Çevirim mükemmel olmayabilir, eğer kötü olduğunu düşünüyorsan bu yorumu eksile ve yorumu sileyim.)" + "\n\n" + "[INFO](https://www.reddit.com/user/translaterobot/comments/pq1kz0/merhabaaa_ben_translaterobot_tr/)")
       
      elif lang_code_f == "fr":
        p_type.reply("*Beep boop, voici ta traduction:* " + "\n\n" + text_output + " \n\n " + "^(Je suis un bot et cette action a été effectuée automatiquement. Ma traduction n'est peut-être pas parfaite, downvote ce commentaire si cette traduction est nulle et je m'en irai.)" + "\n\n" + "[INFO](https://www.reddit.com/user/translaterobot/comments/pq1pdf/helloooo_i_am_translaterobot_en/)")

      elif lang_code_f == "es":
        p_type.reply("*Beep boop, aquí está tu traducción:* " + "\n\n" + text_output + " \n\n " + "^(Soy un bot y esta acción se realizó automáticamente. Es posible que mi traducción no sea perfecta, downvote este comentario si esta traducción apesta y me iré.)" + "\n\n" + "[INFO](https://www.reddit.com/user/translaterobot/comments/pq1pdf/helloooo_i_am_translaterobot_en/)")

      elif lang_code_f == "it":
        p_type.reply("*Beep boop, ecco la tua traduzione:* "  + "\n\n" +   text_output + " \n\n " + "^(Sono un bot e questa azione è stata eseguita automaticamente. La mia traduzione potrebbe non essere perfetta, downvote commento se questa traduzione fa schifo e me ne andrò.)" + "\n\n" + "[INFO](https://www.reddit.com/user/translaterobot/comments/pq1pdf/helloooo_i_am_translaterobot_en/)")

      elif lang_code_f == "de":
        p_type.reply("*Beep boop, hier ist deine übersetzung:* "  + "\n\n" +  text_output + " \n\n " + "^(Ich bin ein Bot und diese Aktion wurde automatisch ausgeführt.Meine Übersetzung ist möglicherweise nicht perfekt.Downvote Sie diesen Kommentar ab, wenn diese Übersetzung scheiße ist, und ich werde weggehen.)" + "\n\n" + "[INFO](https://www.reddit.com/user/translaterobot/comments/pq1pdf/helloooo_i_am_translaterobot_en/)")

      else:
        p_type.reply("*Beep boop, here is your translation:* "  + "\n\n" +  text_output + " \n\n " + "^(I am a bot and this action was performed automatically.My translation may not be perfect,downvote this comment if this translation sucks and I will go away.)" + "\n\n" + "[INFO](https://www.reddit.com/user/translaterobot/comments/pq1pdf/helloooo_i_am_translaterobot_en/)")
                  
                  
  else:
    print("Invalid language code.Passed.")
    p_type.reply("*Your language code was invalid.Please try again with correct language code.[Here is a link if you need help](https://cloud.google.com/translate/docs/languages)* "  + "\n\n" + "^(I am a bot and this action was performed automatically.)" + "\n\n" + "[INFO](https://www.reddit.com/user/translaterobot/comments/pq1pdf/helloooo_i_am_translaterobot_en/)")
              
  print("Replied to " + p_type.id)

                
def main(reddit):
    
  print("Checking for mentions...")

  for mention in reddit.inbox.mentions(limit = 5):
    if mention.new:  
      mention.mark_read()
      list = []
      if  hasattr(mention, "parent_id") and mention.author != reddit.user.me():
        time.sleep(1)
        comment = reddit.comment(id= mention.parent_id)
        if hasattr(comment , "body"):
          reply(mention, comment.body)

          list.append(mention.id)

      if hasattr(mention, "submission") and mention.id not in list and mention.author != reddit.user.me():
        time.sleep(1)
        submission = mention.submission  
        submission_input = "**" + submission.title + "**" +  "\n\n"  + submission.selftext
        reply(mention, submission_input)

    time.sleep(1)

    
  print("Checking for mentions completed.")
 
  time.sleep(2)
  

  print("Checking for comment replies...")
  for replies in reddit.inbox.comment_replies():
    if replies.new:
      reply_l = replies.body.lower()
      if "good bot" in reply_l:
        print("Replied to 'good bot' comment.")
        replies.reply("good human 😊 ")

      elif "bad bot" in reply_l:
        print("Replied to 'bad bot' comment.")
        replies.reply("bad human 😠 ")
      replies.mark_read()

  print("Checking for comment replies completed. ")

  time.sleep(2)

  print("Checking for downvoted comments...")
  redditor = reddit.redditor('translaterobot')
  for comment in redditor.comments.new(limit=10):       
    if comment.score <= -2:
      comment.delete()
      print("Downvoted comments are deleted")

  print("Checking for downvoted comments completed.") 

  print("Sleeping for 15 seconds...")
  time.sleep(15)


reddit = login()

while True:
  try:
    main(reddit)
  except Forbidden:
    print("Banned from this subreddit,skipping...")
    time.sleep(2)
  except Exception as e:
    print(str(e) + " ,sleeping 120 seconds...")
    time.sleep(120)
    
