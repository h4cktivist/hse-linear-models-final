import streamlit as st
import pandas as pd

from PIL import Image

from eda import preprocess_data


st.set_page_config(page_title='', layout='wide')
df = preprocess_data()

st.title(':bank: Склонность клиентов давать положительный ответ на предложение банка')
st.write('Один из способов повысить эффективность взаимодействия банка с клиентами — отправлять предложение о новой '
         'услуге не всем клиентам, а только некоторым, которые выбираются по принципу наибольшей склонности к отклику '
         'на это предложение.')
st.write('Задача заключается в том, чтобы предложить алгоритм, который будет выдавать склонность клиента к '
         'положительному или отрицательному отклику на предложение банка. Предполагается, что, получив такие оценки '
         'для некоторого множества клиентов, банк обратится с предложением только к тем, от кого ожидается '
         'положительный отклик.')
st.write('Для решения данной задачи были взяты персональные данные о клиентах некоторого банка, такие как пол, '
         'зарабток, количество детей и другие.')
st.write('Данные были предварительно обработаны и представлены в виде следующего датасета:')
st.write(df)
st.write(
    '''
- `AGREEMENT_RK` — уникальный идентификатор объекта в выборке;
- `TARGET` — целевая переменная: отклик на маркетинговую кампанию (1 — отклик был зарегистрирован, 0 — отклика не было);
- `AGE` — возраст клиента;
- `SOCSTATUS_WORK_FL` — социальный статус клиента относительно работы (1 — работает, 0 — не работает);
- `SOCSTATUS_PENS_FL` — социальный статус клиента относительно пенсии (1 — пенсионер, 0 — не пенсионер);
- `GENDER` — пол клиента (1 — мужчина, 0 — женщина);
- `CHILD_TOTAL` — количество детей клиента;
- `DEPENDANTS` — количество иждивенцев клиента;
- `PERSONAL_INCOME` — личный доход клиента (в рублях);
- `LOAN_NUM_TOTAL` — количество ссуд клиента;
- `LOAN_NUM_CLOSED` — количество погашенных ссуд клиента.
    '''
)

tab1, = st.tabs([':chart_with_upwards_trend: Анализ'])

with tab1:
    st.write(df.describe())

    st.image(Image.open('app/images/distr.png'))
    st.write('Возраст клиентов банка распределен равномерно, в выборке присутствует каждая из возрастных групп')

    st.image(Image.open('app/images/income.png'))
    st.write('Персональный доход клиентов варируется от 24 до 250000 рублей Медиана равна 13854 рублей. Присутствуют '
             'выбросы')

    st.image(Image.open('app/images/gender-tar.png'))
    st.write('В целом мужчины и женщины почти одинаково склонны давать положительный ответ на предложения банка, '
             'однако женщины делают это немного чаще, чем мужчины')

    st.image(Image.open('app/images/socw-tar.png'))
    st.write('Люди, имеющие работу, дают положительный ответ намного чаще, чем безработные')

    st.image(Image.open('app/images/socp-tar.png'))
    st.write('Подобная картина наблюдается и среди работающих людей и ушедших на пенсию. Пенсионеры с меньшей '
             'вероятностью отвечают согласием на предложения банка, в отличие он ещё работающих людей')

    st.image(Image.open('app/images/flpr-tar.png'))
    st.write('В то время наличие в собственности квартиры почти не влияет на ответ клиента. Согласиться на '
             'предложение банка почти одинаково готовы как имеющие в собственности недвижимость, так и не имеющие')

    st.image(Image.open('app/images/child-tar.png'))
    st.write('Говоря о наличии у клиентов детей, можно заметить, что клиенты, имеющие от 1 до 6 детей реагирют '
             'положительно с большей вероятностью, в отличие от клиентов, имеющих 7-8 детей, которые вовсе не дали '
             'положительного ответа. Однако большинство положительных ответов поступало от клинетов, имеющих 10 детей')

    st.image(Image.open('app/images/deps-tar.png'))
    st.write('С количеством иждивенцев наблюдается немного иная картина. Вероятность положительного отклика линейно '
             'растет, начиная от 0 до 4 иждивенцев. Большинство положительных ответов дали клиенты с 5 и 6 иждивенцами')

    st.image(Image.open('app/images/auto-tar.png'))
    st.write('Не имеющие автомобиля люди или имеющие всего один дают больше положительных откликов')

    st.image(Image.open('app/images/tloan-tar.png'))
    st.image(Image.open('app/images/cloan-tar.png'))
    st.write('Картина с наличием кредитов и количеством закрытых кредитов в целом схожа. Наибольшее количество '
             'положительных отзывов поступало от клиентов, имеющих 8 кредитов в общем или 8 закрытых кредитов')

    st.image(Image.open('app/images/matrix.png'))
    st.write('Была так же построена матрица корреляций, между различными признаками в выборке, из которой можно '
             'сделать следующие выводы: ')
    st.write('''
    - Наибольшая положительная взаимосвязь наблюдается между общим количеством кредитов и количеством закрытых из них (0.86)
    - Значимая взаимосвязь так же наблюдается между пенсионным статусом и возрастом клиента (0.56)
    - Так же взаимосвязь имеет место между количеством детей и количеством иждивенцев (0.51)
    - Наибольшая отрицательная взаимосвязь наблюдается между соц. статусом относительно работы и пенсии (-0.8)
    - Так же отрицательно взаимосвязаны возраст с соц. стаутс относительно работы (-0.45)
    ''')
