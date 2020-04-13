import json
import requests
import html
import webbrowser
import subprocess

counter1 = 0
counter_gesammt = 0
urls = ["/",
"/ausbildung/",
"/ausbildung/bachelor-of-engineering-studiengang-informationstechnik-mwd",
"/ausbildung/fachinformatik-anwendungsentwicklung-mwd",
"/ausbildung/fachinformatik-systemintegration-mwd",
"/bestellen/agb.php",
"/bestellen/domainangebote.php",
"/bestellen/softwareangebote.php",
"/bestellen/warenkorb.php",
"/groupware/",
"/hosting/",
"/hosting/qualitaetsgarantien.php",
"/hosting/webhosting-application-hosting.php",
"/hosting/webhosting-testaccount.php",
"/jobs/",
"/jobs/junior-php-developer-mwd",
"/jobs/software-engineer-mwd-faoer-rd-go-python",
"/jobs/supportmitarbeiter-mwd",
"/jobs/systemadministrator-mit-fokus-auf-linux-und-3rd-level-support-mwd",
"/kontakt/",
"/kontakt/datenschutzerklaerung.php",
"/kontakt/impressum.php",
"/kontakt/postanschrift.php",
"/kontakt/telefonsupport.php",
"/professional/",
"/professional/dedizierte-server/",
"/professional/dedizierte-server/perc_raid_controller.php",
"/professional/dedizierte-server/remote_management.php",
"/professional/individuelle-loesungen/",
"/professional/individuelle-loesungen/penetrationtesting.php",
"/professional/individuelle-loesungen/preise.php",
"/professional/individuelle-loesungen/servermanagement.php",
"/professional/individuelle-loesungen/software-installationen.php",
"/professional/managed-server/managed-cloud-cluster.php",
"/professional/managed-server/managed-privateserver.php",
"/professional/managed-server/managed-server.php",
"/ssl-zertifikate/",
"/ssl-zertifikate/geotrust.php",
"/ssl-zertifikate/globe.php",
"/ssl-zertifikate/rapid.php",
"/ssl-zertifikate/thawte.php",
"/support/",
"/ueber-netcup/",
"/ueber-netcup/auszeichnungen.php",
"/ueber-netcup/ddos-schutz-filter.php",
"/ueber-netcup/hardware-infrastruktur.php",
"/ueber-netcup/kundenmeinungen-netcup.php",
"/ueber-netcup/merchandising.php",
"/ueber-netcup/oekostrom.php",
"/ueber-netcup/partner.php",
"/ueber-netcup/public-relations.php",
"/ueber-netcup/rechenzentrum.php",
"/ueber-netcup/referenzen.php",
"/vserver/",
"/vserver/reseller_angebote_vserver.php",
"/vserver/root-server-erweiterungen.php",
"/vserver/storagespace.php",
"/vserver/uebersicht_vserver_angebote.php",
"/vserver/vergleich-linux-vserver-kvm.php",
"/vserver/vergleich-root-server-vps.php",
"/vserver/vps.php",
"/vserver/vserver_guenstig_qualitaet.php",
"/vserver/vserver_images.php",
"/vserver/vstorage.php"
]
print("===========================")
print("Suchlauf gestartet !")
print("===========================")
for u in urls:
  api = "https://www.netcup.de/api/eggs"

  data = {"requrl": u}
  response = requests.post(api, data).text
  response_json = json.loads(response)
  if response_json["eggs"] != False:
    counter_gesammt = counter_gesammt + 1
    if response_json["eggs"][0]["title"].find("tzguhiohoiuh") == -1: ##dummyline for counter1   
     if response_json["eggs"][0]["title"].find("Domain") == -1:    
      if response_json["eggs"][0]["title"].find("Failover") == -1:
        if response_json["eggs"][0]["title"].find("Webhosting") == -1:    
          if response_json["eggs"][0]["title"].find("Man. Pr") == -1:    
            if response_json["eggs"][0]["title"].find("Managed ") == -1:    
              if response_json["eggs"][0]["title"].find("Reseller") == -1:
                if response_json["eggs"][0]["title"].find("20%") == -1:
                  if response_json["eggs"][0]["title"].find("vLAN") == -1:
#                    if response_json["eggs"][0]["title"].find("8000 SSD") == -1:
#                      if response_json["eggs"][0]["title"].find("4000 SSD") == -1:
        #                if response_json["eggs"][0]["title"].find("2000 SSD") == -1:
       #                   if response_json["eggs"][0]["title"].find("Mega-Ei") == -1:
      #                      if response_json["eggs"][0]["title"].find("Monster-Ei") == -1:      
    #                         if response_json["eggs"][0]["title"].find("VPS Ostern XXL") == -1:
    #                            if response_json["eggs"][0]["title"].find("VPS Ostern S") == -1:
   #                               if response_json["eggs"][0]["title"].find("VPS Ostern M") == -1:
  #                                  if response_json["eggs"][0]["title"].find("VPS Ostern XL") == -1:
 #                                    if response_json["eggs"][0]["title"].find("VPS Ostern L") == -1: 
#                                       if str(response_json["eggs"][0]["product_id"]).find("2576") == -1: 
                                        if str(response_json["eggs"][0]["product_id"]).find("2573") == -1: 
#                                          if str(response_json["eggs"][0]["product_id"]).find("2572") == -1: 
                                            if str(response_json["eggs"][0]["product_id"]).find("2574") == -1: 
#                                             if str(response_json["eggs"][0]["product_id"]).find("2593") == -1: 
                                               if str(response_json["eggs"][0]["product_id"]).find("2578") == -1: 
                                                                                    counter1 = counter1 + 1
                                                                                    print("")
                                                                                    print(str(counter1) + ") Gefunden auf:", "https://netcup.de" + u)
                                                                                    print(html.unescape(response_json["eggs"][0]["title"]), "( Produkt ", str(response_json["eggs"][0]["product_id"]) ,") für", html.unescape(response_json["eggs"][0]["price"]))	
print("---------")                                      
print("===========================")
print(str(counter1) + "/" + str(counter_gesammt) + " Ergebnisse")
print("===========================")
print("DONE!")
print("===========================")
