from validate_email import validate_email

emails = ['example@example.com','exemplo.com.br', '', '123@exemplo.com', '@teste', 'teste@', 'teste@exemplo', 'teste@@exemplo.com', 'teste @exemplo.com', 'teste@ exemplo.com']
def validateEmail(emailAddress):
    return validate_email(emailAddress)


for values in emails:
    if (validateEmail(values)):
        print('The e-mail ' + values + ' is valid.')
    else:
        print('The e-mail ' + values + ' ISNT valid')
