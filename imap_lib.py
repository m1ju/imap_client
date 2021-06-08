from imapclient import IMAPClient
import email, json

'''
@brief
email_id, email_pwd : 메일서버의 계정 정보
mail_server : 메일서버
'''
def IMAP_client(email_id : str, email_pwd : str, mail_server : str):
    with IMAPClient(host=mail_server) as client:
        
        client.login(email_id, email_pwd) # 계정정보
        client.select_folder('INBOX')
        
        messages = client.search(['NOT', 'DELETED'])
        response = client.fetch(messages, ['RFC822'])

        mail_list = []

        for message_id, data in response.items():
            MSG = email.message_from_bytes(data[b'RFC822']) # mail 파싱

            print('-' * 30)
            # Header
            print('id : {id}'.format(id=message_id))
            print('From : {From}'.format(From=MSG.get('From')))
            print('To : {To}'.format(To=MSG.get('TO')))
            print('CC : {CC}'.format(CC=MSG.get('CC')))
            print('Subject : {subject}'.format(subject=MSG.get('Subject')))
            print('Date : {Date}'.format(Date=MSG.get('Date')))
            # Body
            print('BODY : {BODY}'.format(BODY=MSG.get('BODY')))
                
        return mail_list
