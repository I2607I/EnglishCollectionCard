def gen_template(code):
    template = f'''<div style="background-color: lightblue; padding: 20px;">
                <div style="background-color: white; padding: 10px;">
                Введите проверочный код {code}
                </div>
                </div>
                '''
    return template