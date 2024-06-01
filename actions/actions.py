# This file contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionFromIndia(Action):
    def name(self) -> Text:
        return "action_from_india"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Study semester abroad admission - Indian")

        return []

class ActionFromEurope(Action):
    def name(self) -> Text:
        return "action_from_europe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="The Bavarian State Ministry supports academic education and therefore charges no tuition fees for all full-time EU/EEA students. "
                 "We only charge a small student services fee of 72€ per semester for full-time EU/EEA students")

        return []

class ActionPaymentInfo(Action):
    def name(self) -> Text:
        return "action_payment_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="In accordance with the DIT's fee regulations (currently only available in German),"
                 "each semester you need to pay a student service fee of 72€  "
                 "+ additional administration and support fees of 500€ that will be charged to international students"
                 " starting from the winter semester 2024/2025")

        return []


class ActionUniversityWebsite(Action):
    def name(self) -> Text:
        return "action_university_website"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="The official website of the Technische Hochschule Deggendorf is: https://www.th-deg.de")

        return []

class ActionEventDetails(Action):
    def name(self) -> Text:
        return "action_event_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="Every year, we host an open house event that provides prospective students and their families "
                 "with an opportunity to explore our university and experience the dynamic atmosphere "
                 "of our campus firsthand. "
                 "Here are the upcoming events: https://www.th-deg.de/en/students/going-abroad/event-calender")

        return []

class ActionExchangeRequirements(Action):
    def name(self) -> Text:
        return "action_exchange_requirements"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="This depends on each case and on each study program."
                 "For more information visit this website: https://www.service4mobility.com/thdeg/BewerbungServlet?identifier=DEGGEND01&kz_bew_art=OUT&kz_bew_pers=S&aust_prog=SMS&sprache=en."
                 "Please send an email to welcome@th-deg.de.")

        return []

class ActionExchangeApplication(Action):
    def name(self) -> Text:
        return "action_exchange_application"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="I can provide information about the application process. "
                 "Please visit our official website or contact our admission office for detailed instructions. "
                 "Follow this link: https://www.th-deg.de/Studierende/Auslandsstudium/semester-abroad-en.pdf")
        return []


class ActionApplicationDeadline(Action):
    def name(self) -> Text:
        return "action_application_deadline"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="The annual deadline is February 15th for an exchange semester in the following academic year (winter and summer semester). "
                 "In mid-March, all applicants will be informed via email about the partner university they've been accepted to and further documents needed to be submitted to the International Office in B 210 to secure their place. "
                 "After nomination by the university: submit Learning Agreement (external and internal) along with the application documents for your host university to the International Office.")
        return []

class ActionCoursesInfo(Action):
    def name(self) -> Text:
        return "action_courses_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="To find more about the courses offered and list of partner universities, "
                 "please visit: https://www.th-deg.de/Studierende/Auslandsstudium/partnerunis_studenten.pdf")
        return []

class ActionInternshipInfo(Action):
    def name(self) -> Text:
        return "action_internship_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="The compulsory internship or a short internship during the semester break can be completed abroad. "
                 "Both possibilities are explained in detail on iLearn. "
                 "Please clarify regulations specified by the Administration Centre. "
                 "You can find more information here: https://ilearn.th-deg.de/course/view.php?id=5664")
        return []

class ActionInternshipPreparation(Action):
    def name(self) -> Text:
        return "action_internship_preparation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="To prepare for your internship abroad, consider attending these events that take place every semester: "
                 "1. Five steps to an international internship "
                 "2. “Creating an English CV” seminar. "
                 "You can also organize a CV check for your English CV with Romy Geiger. "
                 "Contact: romy.geiger@th-deg.de")
        return []

class ActionShortInternshipInfo(Action):
    def name(self) -> Text:
        return "action_short_internship_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="A short work experience is more about gaining intercultural competence and knowledge of the German language, "
                 "so keep your mind open and also consider a voluntary job. "
                 "You'll learn German fast if you work!")
        return []

class ActionCompulsoryInternshipInfo(Action):
    def name(self) -> Text:
        return "action_compulsory_internship_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="1. Worldwide internships: "
                 "After attending the introductory event, arrange a personal consultation to clarify individual inquiries and check iLearn. "
                 "Company vacancies can be found on the DIT online job board. "
                 "Additionally, you can apply to the International Office for funding or scholarships. "
                 "2. European internships: "
                 "Students intending to undertake a 60+ day internship in Europe or Iceland, Liechtenstein, Norway, or Turkey can apply for a scholarship via the International Office. "
                 "Your internship salary or financial situation is NOT relevant! "
                 "Please contact Romy Geiger in the International Office. "
                 "Student-to-student exchange can be viewed on the DAAD EU-community website.")
        return []

class ActionSummerSchoolInfo(Action):
    def name(self) -> Text:
        return "action_summer_school_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="Apart from studying abroad or doing an internship abroad, it is also possible to visit a summer school (usually 3-8 weeks) in a foreign country. "
                 "The summer school program often includes specialized courses, language courses, and information about the country and its culture. "
                 "There may also be excursions. "
                 "It does not substitute for the semester abroad but is a great additional opportunity to go abroad.")

        return []

class ActionSummerSchoolFunding(Action):
    def name(self) -> Text:
        return "action_summer_school_funding"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
                        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="If you are an enrolled DIT student, there are several opportunities to partially finance your semester abroad through a scholarship. "
                 "As all scholarship programs outlined here are administered in the International Office, you only need to submit ONE application. "
                 "Applications can be submitted to the International Office; there is no defined application deadline. "
                 "Required documents: "
                 "1. Application form "
                 "2. CV in tabular form "
                 "3. Financial plan "
                 "4. Current transcript (grade sheet) "
                 "5. Passport photo "
                 "6. Internship contract, if applicable")

        return []

class ActionErasmusInfo(Action):
    def name(self) -> Text:
        return "action_erasmus_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="Erasmus+ is a European scholarship program that supports, promotes, and funds student mobility across Europe. "
                 "Students in the Erasmus+ program study for at least 3 months or complete an internship for at least 2 months in another European country. "
                 "More information on Erasmus+ can be found here: https://www.th-deg.de/en/students/going-abroad#erasmus+")

        return []

class ActionStudentIDCardInfo(Action):
    def name(self) -> Text:
        return "action_student_ID_card_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="The ISIC card is valid for one year and costs 15 euros. "
                 "Apply for the ISIC card directly on the [ISIC website](https://www.isic.de). "
                 "Follow the 'get your card' link.")

        return []


class ActionContactInfo(Action):
    def name(self) -> Text:
        return "action_contact_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="You can contact DIT International Office at international.office@th-deg.de. "
                 "Alternatively, you can visit the DIT website to find more information. "
                 "Please use this email to contact the international office: romy.geiger@th-deg.de")

        return []

class ActionCheckingIn(Action):
    def name(self) -> Text:
        return         "action_checking_in"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Do you need any more assistance? If you have further questions about studying abroad, feel free to ask. "
                 "Otherwise, goodbye and best of luck with your application!")

        return []



