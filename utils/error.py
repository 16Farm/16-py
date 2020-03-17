from colorama import init, Fore, Style
init(autoreset=True)

errors = ['invalid_token', 'client_version/new_client_version_exists', 'oauth2_mac_rails/link_code_not_found', 'already_accepted_mission_rewards', 'act_is_not_enough', 'the_number_of_cards_must_be_less_than_or_equal_to_the_capacity', 'no_condition_to_try_the_quest_is_fulfilled', 'invalid_area_conditions_potential_releasable', 'active_record/record_not_found', 'invalid_only_card_quest_limitation_conditions', 'invalid_requiring_card_quest_limitation_conditions', 'z_battle_check_point_does_not_exist', 'invalid_only_element_quest_limitation_conditions', 'invalid_allowed_category_quest_limitation_conditions', 'invalid_requiring_element_quest_limitation_conditions', 'visited_count_of_the_quest_reaches_the_limit', 'oauth2_mac_rails/client_transferred', 'act_is_already_maximum', 'already_linked_facebook_by_others', 'user_comeback_campaign_is_not_found']

def Handler(source, response):
    global errors
    if 'code' in response['error']:
        if str(response['error']['code']) in errors:
            if response['error']['code'] == 'client_version/new_client_version_exists':
                print(Fore.LIGHTRED_EX + 'New app update available!')
            if response['error']['code'] == 'oauth2_mac_rails/link_code_not_found':
                print(Fore.LIGHTRED_EX + 'Transfer code not found!')
            if response['error']['code'] == 'oauth2_mac_rails/client_transferred':
                print(Fore.LIGHTRED_EX + 'Account was transferred elsewhere!')
            if response['error']['code'] == 'already_accepted_mission_rewards':
                print(Fore.LIGHTRED_EX + 'You\'ve ready claimed!')
            if response['error']['code'] == 'act_is_not_enough':
                print(Fore.LIGHTRED_EX + 'Low on stamina!')
            if response['error']['code'] == 'the_number_of_cards_must_be_less_than_or_equal_to_the_capacity':
                print(Fore.LIGHTRED_EX + 'Box capacity exceeded!')
            if response['error']['code'] == 'no_condition_to_try_the_quest_is_fulfilled':
                print(Fore.LIGHTRED_EX + 'Area not unlocked or found!')
            if response['error']['code'] == 'invalid_area_conditions_potential_releasable':
                print(Fore.LIGHTRED_EX + 'Potential isn\'t unlocked!')
            if response['error']['code'] == 'active_record/record_not_found':
                print(Fore.LIGHTRED_EX + 'Not active or found!')
            if response['error']['code'] == 'invalid_only_card_quest_limitation_conditions':
                print(Fore.LIGHTRED_EX + 'Team does not meet stage conditions!')
            if response['error']['code'] == 'invalid_requiring_card_quest_limitation_conditions':
                print(Fore.LIGHTRED_EX + 'Team does not have required Card(s)!')
            if response['error']['code'] == 'z_battle_check_point_does_not_exist':
                print(Fore.LIGHTRED_EX + 'Level not unlocked or already cleared!')
            if response['error']['code'] == 'invalid_only_element_quest_limitation_conditions':
                print(Fore.LIGHTRED_EX + 'Team Type does not meet conditions!')
            if response['error']['code'] == 'invalid_allowed_category_quest_limitation_conditions':
                print(Fore.LIGHTRED_EX + 'Team Category does not meet conditions!')
            if response['error']['code'] == 'invalid_requiring_element_quest_limitation_conditions':
                print(Fore.LIGHTRED_EX + 'Team does not have required Type(s)!')
            if response['error']['code'] == 'visited_count_of_the_quest_reaches_the_limit':
                print(Fore.LIGHTRED_EX + 'Maximum runs for this stage reached!')
            if response['error']['code'] == 'act_is_already_maximum':
                print(Fore.LIGHTRED_EX + 'Stamina already full!')
            if response['error']['code'] == 'already_linked_facebook_by_others':
                print(Fore.LIGHTRED_EX + 'Facebook is linked to another dokkan!')
            if response['error']['code'] == 'user_comeback_campaign_is_not_found':
                print(Fore.LIGHTRED_EX + 'No hercule/comeback campaign active!')
        else:
            print(Fore.LIGHTRED_EX + str(source) + ' > error occurred:')
            print(Fore.LIGHTRED_EX + '"' + str(response) + '"\nPlease send a screenshot of this error to the Discord.')
    else:
        if str(response['error']) in errors:
            if 'invalid_token' in response['error']:
                print(Fore.LIGHTRED_EX + 'Session has expired!')
            if 'unauthorized' in response['error']:
                print(Fore.LIGHTRED_EX + '[Unauthorized] You can\'t access servers... perhaps use a VPN?')
        else:
            print(Fore.LIGHTRED_EX + str(source) + ' > error occurred:')
            print(Fore.LIGHTRED_EX + '"' + str(response) + '"\nPlease send a screenshot of this error to the Discord.')