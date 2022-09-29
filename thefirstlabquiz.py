class urunler:
    #we're idefentifying attributes in this step:
    urun_adi: str = ""
    urun_alis_fiyati: float = 0
    urun_otv_orani:float = 0
    urun_kdv_orani:float = 0

    #we're creating a constructor for class of urunler in this step:                                            #these are words in English. I'm writing for wanting everyone understand the code.
    def __init__(self,urun_adi, urun_alis_fiyati, urun_otv_orani, urun_kdv_orani) :                             # urun_adi = product_name
        self.urun_adi = urun_adi                                                                                # urun_alis_fiyati = product_purchase_price
        self.urun_alis_fiyati = urun_alis_fiyati                                                                # urun_otv_orani = product_tax_rate // otv = a tax in Turkey
        self.urun_otv_orani = urun_otv_orani                                                                    # urun_adi = product_tax_rate // kdv = a tax in Turkey
        self.urun_kdv_orani = urun_kdv_orani                                                                    # sfiyati = saleprice
                                                                                                                # kar_orani = profit rate
        #the method is created for calculating system                                                           # elma = bread, patates = patato, un = fame, yumurta = egg
    def urun_satis_fiyati(self,kar_orani):                                                                      # toplam = sum / total -> the variable created for calculate total basket.
        sfiyati = self.urun_alis_fiyati
        sfiyati = sfiyati + (sfiyati * kar_orani)
        sfiyati = sfiyati + (sfiyati * self.urun_otv_orani)
        sfiyati = sfiyati + (sfiyati * self.urun_kdv_orani)
        return sfiyati 


        #the fuction is created for calculating for all basket.
def sepet_fiyati(kar_orani):
    ekmek=urunler('ekmek',1,0.20,0.12)
    patates=urunler('patates',2,0.16,0.18)
    elma=urunler('elma',3,0.11,0.22)
    un=urunler('un',4,0.17,0.05)
    yumurta=urunler('yumurta',5,0.30,0.19)
    toplam=0
    toplam = toplam + ekmek.urun_satis_fiyati(kar_orani)
    toplam = toplam + patates.urun_satis_fiyati(kar_orani)
    toplam = toplam + elma.urun_satis_fiyati(kar_orani)
    toplam = toplam + un.urun_satis_fiyati(kar_orani)
    toplam = toplam + yumurta.urun_satis_fiyati(kar_orani)
    return toplam

    #the function is created for verifying the total of basket value. 
    #If the output is true: our code is true
    #If the output is false: our code has some mistakes.

def odev_test():
    sepet_toplam = sepet_fiyati(0.15)
    if sepet_toplam==23.91218:
        print("true")
    else:
        print("false")


#We're using the method for running the function to verifying the total of basket value.
odev_test()
