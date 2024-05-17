#
# import logging
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     filename='logs.log',
#     filemode='w',
#     format='%(asctime)s - [5(levelname)s] - 5(message)s'
# )
#
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
#
# try:
#     print(10 / 0)
# except Exception as err:
#     logging.exception(err)




# if 2 + 2 == 4:
#     print('this is fact - 2 + 2 = 4')
#
#
# assert 2 + 2 == 4
# assert 2 + 2 == 5, 'wrong'

# """
# >>> 2 + 2
# 5
# """
#
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

def adder(*args, **kwargs):
    result = 0
    for _ in args:
        if type(_) in (int, float, bool):
            result += _
        else:
            try:
                result += float(_)
                continue
            except (ValueError, TypeError):
                pass

            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass

    for _ in kwargs.values():
        if type(_) in (int, float, bool):
            result += _
        else:
            try:
                result += float(_)
                continue
            except (ValueError, TypeError):
                pass

            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass
    return result