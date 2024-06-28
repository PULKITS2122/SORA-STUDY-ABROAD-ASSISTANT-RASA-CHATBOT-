# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionIndian(Action):
    def name(self) -> Text:
        return "action_indian"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Study semester abroad admission - indian")

        return []

class ActionEuropean(Action):
    def name(self) -> Text:
        return "action_european"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="The Bavarian State Ministry supports academic education and therefore charges no tuition fees for all full-time EU/EEA students. "
                 "We only charge a small student services fee of 72€ per semester for full-time EU/EEA students")

        return []

class ActionPay(Action):
    def name(self) -> Text:
        return "action_pay"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="In accordance with the DIT's fee regulations (currently only available in German),"
                 "each semester you need to pay a student service fee of 72€  "
                 "+ additional administration and support fees of 500€ that will be charged to international students"
                 " starting from the winter semester 2024/2025")

        return []


class ActionUniWebsite(Action):
    def name(self) -> Text:
        return "action_uni_website"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="The official website of the Technische Hochschule Deggendorf is: https://www.th-deg.de")

        return []

class ActionEventInfo(Action):
    def name(self) -> Text:
        return "action_events_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="Every year, we host an open house event that provides prospective students and their families "
                 "with an opportunity to explore our university and experience the dynamic atmosphere "
                 "of our campus firsthand. "
                 "Here are the upcoming events: https://www.th-deg.de/en/students/going-abroad/event-calender")

        return []

class ActionSemesterAbroadAdmissionRequirements(Action):
    def name(self) -> Text:
        return "action_semester_abroad_admission_requirements"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="This depends on each case and on each study program."
                 "For more information visit this website: https://www.service4mobility.com/thdeg/BewerbungServlet?identifier=DEGGEND01&kz_bew_art=OUT&kz_bew_pers=S&aust_prog=SMS&sprache=en."
                 "Please send an email to welcome@th-deg.de.")

        return []

class ActionSemesterAbroadApplicationProcess(Action):
    def name(self) -> Text:
        return "action_semester_abroad_application_process"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="I can provide information about the application process. "
                 "Please visit our official website or contact our admission office for detailed instructions. "
                 "Follow this link: https://www.th-deg.de/Studierende/Auslandsstudium/semester-abroad-en.pdf")
        return []


class ActionSemesterAbroadApplicationDeadline(Action):
    def name(self) -> Text:
        return "action_semester_abroad_application_deadline"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="I can provide information about the application process deadline.")
        return []

class ActionAvailableCourses(Action):
    def name(self) -> Text:
        return "action_available_courses"

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
            text="To find more about the internship information, "
                 "please visit: https://www.th-deg.de/en/students/going-abroad#internship-abroad")
        return []

class ActionInternshipPreparationInfo(Action):
    def name(self) -> Text:
        return "action_internship_preparation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="To find more about the Internship Preparation information, "
                 "please contact: [Romy Geiger] romy.geiger@th-deg.de")
        return []

class ActionShortInternshipInfo(Action):
    def name(self) -> Text:
        return "action_internship_short"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Questions regrading the short term internship.")
        return []

class ActionCompulsoryInternshipInfo(Action):
    def name(self) -> Text:
        return "action_internship_compulsory"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Questions regrading the compulsory term internship. "
                 "Please visit: https://www.th-deg.de/en/students/going-abroad#internship-abroad")
        return []

class ActionSummerSchoolInfo(Action):
    def name(self) -> Text:
        return "action_summer_school_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="Question regarding admission to Summer School.")

        return []

class ActionSummerSchoolFunding(Action):
    def name(self) -> Text:
        return "action_summer_funding"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="How can you fund summer school using various scholarship?")

        return []

class ActionErasmusInfo(Action):
    def name(self) -> Text:
        return "action_erasmus_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="Question regarding Erasmus+.")

        return []

class ActionISICInfo(Action):
    def name(self) -> Text:
        return "action_international_student_ID_card_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="How one can register or apply for International Student ID Card (ISIC)?")

        return []


class ActionContactInfo(Action):
    def name(self) -> Text:
        return "action_contact_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="You can contact DIT International Office at international.office@th-deg.de . Alternatively, you can visit the DIT website to find more information. Please use this email to contact the international office: romy.geiger@th-deg.de")

        return []

class ActionAskingEverythingOk(Action):
    def name(self) -> Text:
        return "action_asking_everything_ok"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Do you need any more assistance? If you have further questions about Study semester abroad, feel free to ask. Otherwise, goodbye and best of luck with your application!")

        return []
