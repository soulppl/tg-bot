class ServiceData:
    is_editing = 'is_editing'
    editing_field = 'editing_field'
    last_message = 'last_message'


class Referral:
    referral_nickname = 'referral_nickname'
    referee = 'referee'


class QuizResponsesFields:
    name = "name"
    location = "location"
    interests = "interests"
    travels = "travels"
    about = "about"
    invite_link = "invite_link"
    last_message_id = "last_message_id"
    service_data = ServiceData
    referral = Referral
