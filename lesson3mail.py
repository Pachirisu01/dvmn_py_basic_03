import smtplib
from dotenv import load_dotenv
import os
load_dotenv()


letter = """\
From: Polinova31@yandex.ru
To: Politovmaksim01@yandex.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

letter = letter.replace('%friend_name%', 'Максим')
letter = letter.replace('%my_name%', 'Полина')
letter = letter.replace('%website%', 'https://dvmn.org/profession-ref-program/cocao143/0wBw7/')

letter = letter.encode("UTF-8")



email_from = 'Polinova31@yandex.ru'
email_to = 'Politovmaksim01@yandex.ru'
message = letter
server = smtplib.SMTP_SSL('smtp.yandex.com', 465) 
pogin = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
server.login(login,password)
server.sendmail(email_from, email_to, message)
server.quit()
