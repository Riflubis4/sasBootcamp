#INPUT  => 7

#OUTPUT =>
#    *
#   * *
#  *   *
# *     *
#  *   *
#   * *
#    *


def main():
    size = int(input())
    i = 1

for i in range(0, size):
    for j in range(0, size):
        if j == size - i - 1 or j == size + i - 1 or i == size - 1:
           print('*', end='')
        else:
            print('', end='')
    print('')


        #for k in range(0, 2 * i + 1):
            #print('*', end='')
        #print('')


if __name__ == '__main__':
    main()