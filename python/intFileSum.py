class Solution:
    def fileSum(self,filename):
        
        f = open(filename,'r');
        try:
            sum = 0
            for line in f:
                sum += int(line)
            print sum
        except TypeError:
            print ('WRONG')
        except SystemError:
            print ('WRONG AGAIN')
        except IOError:
            print ('WRONG AGAIN YAAR')
        else:
            print ('All Done')

s = Solution()
s.fileSum('intFile.txt')

            