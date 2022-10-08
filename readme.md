## Problem ID: 616

## Problem Statement: Chatbot for GTU

## Team:

## Leader:

1. Kotak Hiranj Maheshbhai

## Members:

1. Mav Rinkal Dhanesh
2. Keraliya Jay Ashvinbhai
3. Koladiya Hit Bharatbhai
4. Mendpara Henil Nileshbhai
5. Nandani Heli Pankajkumar
6. Kshitiz Pandya Devangbhai
7. Jivrajani Kushal Bipinbhai

## Abstract:

Many chatbots have been developed in the past by various companies for a variety of purposes. But neither the government universities nor the students could benefit from such an official bot. The website has multiple directories that students must navigate through in order to find the syllabus and test dates. Instead, we offer a tailored solution that benefits both the universities and the students. Students will get access to items such as prior year papers, event histories, images, and PDFs as soon as universities upload the data. To obtain information about the payment and result, the student Id will also be registered inside the bot.

## Literature Review:

Alexa and Siri from Apple are the biggest rivals, as we can all agree. Companies have been attempting to use machine learning to construct chat bots for a very long time. Some of them use text- and audio-based platforms. There are no such bots or government facilities. To distribute the materials, the students build an automated bot on Telegram that sends simple papers. This chatbot has evolved through natural level processing and can respond appropriately to any query, even if it is poorly phrased or pertains to a topic for which it was not specifically programmed.

## Approach:

When a user first launches our Telegram bot by typing "/start," he or she will be presented with the bot's main menu, where they will have five options:

1. Admission: Where to send questions about admission to the authority
2. Fees: This is where he or she can get information on the receipt for payments, unpaid fees, etc.
3. Syllabus: This is accessible to users without an enrollment ID, allowing students who are interested in enrolling in GTU to view the syllabus for certain subjects.
4. Exam: All users can access information on the timetable and seating arrangements with a single click.
5. Attendance: After authenticating the student via an OTP, users will be given access to the Attendance.
6. Result: Here, the users can see their respective results after getting authenticated by us via OTP

## Roadmap:

## Tools and technologies

Programming Language: Python
Dialogflow : dialogflow is an NLU(Natural Language Understanding ) platform provided by Google which is used to design and integrate a conversational user interface into your mobile app, web application, device, bot, interactive voice response system, and so on.
Flask : Flask is the microframework written in Python. which is widely used in industries for backend and creating RESTful API.
Telegram : Telegram is a globally accessible freemium, cross-platform, cloud-based instant messaging (IM) service, it also provides the opensource API to create bots.
Firebase : Firebase is a BaaS(Backend as a Service) platform developed by Google which provides the services such as Authentication, Storage, Database etc.
MongoDB: MongoDB is an open-source document database and leading NoSQL database. MongoDB is a highly scalable and performance-oriented database.

## Challenges:

Although we are aware that WhatsApp is the dominant talking programme currently dominating the market, the technology we are utilising does not offer direct interaction with WhatsApp. Twilio Sandbox offered an alternative connection method. It makes the Chatbot more expensive. As a result, we made the decision to switch to Telegram, which offers direct communication with Dialog flow. Additionally, we were unaware of the technology involved because we were not aware that training the chatbot requires ML (Machine Learning) and NLP (Natural Language Processing). As a result, we chose to switch to the Dialog flow, a platform for NLU (natural language understanding).

## Possible outcome of the work

A Chatbot which can used in any platform such as telegram, slack, messenger, web app, etc. which can solve the academics problem for students such as

1. he/she can see his/her Result in our bot
2. he/she can see his/her Attendance in our bot
3. he/she can see exam Time Table in our bot
4. he/she can see the status of his/her fees
   This all things can be viewed by student through his enrolment id by entering otp(one time y
   there are some extra features which can be viewed by student outside of GTU that are
5. he/she can see the syllabus of the course (Branch wise )
6. he/she can send enquiry for Admission to his/her selected colleges(under GTU)
7. he/she can see the details about all the colleges that come under GTU.

## Work done till date

Nearly 50% to 60% of the work has been completed. The most important phase, integrating Dialog flow with Telegram, has been completed and tested to make sure everything is working as it should. The bot has been trained to meet the standards to a degree of over 50%. The syllabus for each department is available to the user. Currently connected to MongoDB, the backend server is ready. However, if another database is required, we will switch to it. For user convenience, the admission inquiry is also created.


## Screenshots
