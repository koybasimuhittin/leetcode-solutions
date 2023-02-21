class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        newSentence = ""
        sentence = sentence.split()
        for i in range(len(sentence)):
            if(sentence[i][0] in vowels):
                newSentence += sentence[i]
            else:
                newSentence += sentence[i][1:] + sentence[i][0]
            newSentence += "ma" + (i + 1) * 'a' + " "
        return newSentence[:-1]