class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int
        :type initialExperience: int
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """

        sumOfEnergy = 1
        neededExperience = 0
        hoursOfTraining = 0

        for e in energy:
            sumOfEnergy += e

        for e in experience:
            if(initialExperience <= e):
                neededExperience += e - initialExperience + 1
                initialExperience = 2 * e + 1
            else:
                initialExperience += e

        hoursOfTraining = neededExperience + max(sumOfEnergy - initialEnergy, 0)
        
        return hoursOfTraining