from django.db import models

class ModelForms(models.Model):
    gender = [('M','Male'),('F','Female')]
    YEARS = [x for x in range(1900,2023)]
    WEIGHT = [('Select','Select'),('Less Than 20','Less Than 20'),('20-40','20-40'),('40-60','40-60'),('60-80','60-80'),('80-100','80-100'),('Greater Than 100','Greater Than 100')]
    PBFC = [('Select','Select'),('Fever',"Fever"),('Cold and Cough',"Cold and Cough"),('Headache',"Headache"),('Stomach Ache',"Stomach Ache"),('Vision Problem',"Vision Problem"),('Dental Issue',"Dental Issue"),('ENT',"ENT"),('Heart Problem',"Heart Problem"),('Liver Issue',"Liver Issue"),('Digestion Problem',"Digestion Problem"),('Others',"Others")]
    DRFC = [('Select','Select'),('Dr. B.S. Gupta',"Dr. B.S. Gupta"),('Dr. Anantha Subramaniam',"Dr. Anantha Subramaniam"),('Dr. Jawahar Ticku',"Dr. Jawahar Ticku "),('Dr. S.K. Agarwal',"Dr. S.K. Agarwal"),('Dr. Bhagwan Swaroop Gupta',"Dr. Bhagwan Swaroop Gupta"),('Dr. Rajesh Patel.',"Dr. Rajesh Patel."),('Dr. Yaghyavalk Sharma.',"Dr. Yaghyavalk Sharma."),('Dr. Prem Sanker.',"Dr. Prem Sanker."),('Dr. Satyendra Chaudhary.',"Dr. Satyendra Chaudhary."),('Dr. Suhail Farooq.',"Dr. Suhail Farooq."),('Dr. Gaurav Mittal.',"Dr. Gaurav Mittal.")]
    Name = models.CharField(max_length=264)
    Age = models.DecimalField(max_digits=2,decimal_places=0)
    Email = models.EmailField()
    BP = models.CharField(max_length=264)
    gender1 = models.CharField(verbose_name='Gender',choices=gender,max_length=264,default='None')
    YEARS1 = models.DateField(verbose_name='Date of Birth')
    WEIGHT1 = models.CharField(verbose_name='Weight',choices=WEIGHT,max_length=264,default='Select')
    PBFC1 = models.CharField(verbose_name='Problems Facing',choices=PBFC,max_length=264,default='Select')
    DRFC1 = models.CharField(verbose_name='Doctor to be Reffered',choices=DRFC,max_length=264,default='Select')

    def __str__(self):
        return self.Name