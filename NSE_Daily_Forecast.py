import pickle
import sklearn as sk
from sklearn.linear_model import LogisticRegression
import pandas as pd
from pandas.tseries.offsets import BDay
import numpy as np
#stocks = ['NSE.NS']
stocks = ['NSE.NS',
'20MICRONS.NS',
'3IINFOTECH.NS',
'3MINDIA.NS',
'5PAISA.NS',
'63MOONS.NS',
'8KMILES.NS',
'A2ZINFRA.NS',
'AARTIDRUGS.NS',
'AARTIIND.NS',
'AARVEEDEN.NS',
'AARVI.NS',
'ABAN.NS',
'ABB.NS',
'ABBOTINDIA.NS',
'ABCAPITAL.NS',
'ABFRL.NS',
'ABGSHIP.NS',
'ABMINTLTD.NS',
'ACC.NS',
'ACCELYA.NS',
'ACCORD.NS',
'ACE.NS',
'ACEINTEG.NS',
'ADANIENT.NS',
'ADANIPORTS.NS',
'ADANIPOWER.NS',
'ADANITRANS.NS',
'ADFFOODS.NS',
'ADHUNIK.NS',
'ADHUNIKIND.NS',
'ADLABS.NS',
'ADORWELD.NS',
'ADSL.NS',
'ADVANIHOTR.NS',
'ADVENZYMES.NS',
'AEGISCHEM.NS',
'AGARIND.NS',
'AGCNET.NS',
'AGLSL.NS',
'AGRITECH.NS',
'AGROPHOS.NS',
'AHLEAST.NS',
'AHLUCONT.NS',
'AHLWEST.NS',
'AIAENG.NS',
'AIFL.NS',
'AIRAN.NS',
'AIROLAM.NS',
'AISL.NS',
'AJANTPHARM.NS',
'AJMERA.NS',
'AKSHARCHEM.NS',
'AKSHOPTFBR.NS',
'AKZOINDIA.NS',
'ALANKIT.NS',
'ALBERTDAVD.NS',
'ALBK.NS',
'ALCHEM.NS',
'ALEMBICLTD.NS',
'ALICON.NS',
'ALKALI.NS',
'ALKEM.NS',
'ALKYLAMINE.NS',
'ALLCARGO.NS',
'ALLSEC.NS',
'ALMONDZ.NS',
'ALOKTEXT.NS',
'ALPA.NS',
'ALPHAGEO.NS',
'ALPSINDUS.NS',
'AMARAJABAT.NS',
'AMBIKCO.NS',
'AMBUJACEM.NS',
'AMDIND.NS',
'AMRUTANJAN.NS',
'AMTEKAUTO.NS',
'ANANTRAJ.NS',
'ANDHRABANK.NS',
'ANDHRACEMT.NS',
'ANDHRSUGAR.NS',
'ANGIND.NS',
'ANIKINDS.NS',
'ANSALAPI.NS',
'ANSALHSG.NS',
'ANTGRAPHIC.NS',
'APARINDS.NS',
'APCL.NS',
'APCOTEXIND.NS',
'APEX.NS',
'APLAPOLLO.NS',
'APLLTD.NS',
'APOLLOHOSP.NS',
'APOLLOTYRE.NS',
'APOLSINHOT.NS',
'APTECHT.NS',
'ARCHIDPLY.NS',
'ARCHIES.NS',
'ARCOTECH.NS',
'ARIES.NS',
'ARIHANT.NS',
'ARIHANTSUP.NS',
'ARMANFIN.NS',
'AROGRANITE.NS',
'ARROWGREEN.NS',
'ARROWTEX.NS',
'ARSHIYA.NS',
'ARSSINFRA.NS',
'ARVIND.NS',
'ARVSMART.NS',
'ASAHIINDIA.NS',
'ASAHISONG.NS',
'ASAL.NS',
'ASHAPURMIN.NS',
'ASHIANA.NS',
'ASHIMASYN.NS',
'ASHOKA.NS',
'ASHOKLEY.NS',
'ASIANHOTNR.NS',
'ASIANPAINT.NS',
'ASIANTILES.NS',
'ASPINWALL.NS',
'ASSAMCO.NS',
'ASTEC.NS',
'ASTRAL.NS',
'ASTRAMICRO.NS',
'ASTRAZEN.NS',
'ATFL.NS',
'ATLANTA.NS',
'ATLASCYCLE.NS',
'ATUL.NS',
'ATULAUTO.NS',
'AUBANK.NS',
'AURDIS.NS',
'AURIONPRO.NS',
'AUROPHARMA.NS',
'AUSOMENT.NS',
'AUTOAXLES.NS',
'AUTOIND.NS',
'AUTOLITIND.NS',
'AVADHSUGAR.NS',
'AVANTIFEED.NS',
'AVTNPL.NS',
'AXISBANK.NS',
'AXISCADES.NS',
'AXISGOLD.NS',
'AXISNIFTY.NS',
'AYMSYNTEX.NS',
'BAFNAPHARM.NS',
'BAGFILMS.NS',
'BAJAJ-AUTO.NS',
'BAJAJCORP.NS',
'BAJAJELEC.NS',
'BAJAJFINSV.NS',
'BAJAJHIND.NS',
'BAJAJHLDNG.NS',
'BAJFINANCE.NS',
'BALAJITELE.NS',
'BALAMINES.NS',
'BALAXI.NS',
'BALKRISHNA.NS',
'BALKRISIND.NS',
'BALLARPUR.NS',
'BALMLAWRIE.NS',
'BALPHARMA.NS',
'BALRAMCHIN.NS',
'BANARBEADS.NS',
'BANARISUG.NS',
'BANCOINDIA.NS',
'BANG.NS',
'BANKBARODA.NS',
'BANKBEES.NS',
'BANKINDIA.NS',
'BANSAL.NS',
'BANSWRAS.NS',
'BARTRONICS.NS',
'BASF.NS',
'BASML.NS',
'BATAINDIA.NS',
'BAYERCROP.NS',
'BBL.NS',
'BBTC.NS',
'BEARDSELL.NS',
'BEDMUTHA.NS',
'BEL.NS',
'BEML.NS',
'BEPL.NS',
'BERGEPAINT.NS',
'BETA.NS',
'BFINVEST.NS',
'BFUTILITIE.NS',
'BGLOBAL.NS',
'BGRENERGY.NS',
'BHAGERIA.NS',
'BHAGYANGR.NS',
'BHAGYAPROP.NS',
'BHANDARI.NS',
'BHARATFIN.NS',
'BHARATFORG.NS',
'BHARATGEAR.NS',
'BHARATIDIL.NS',
'BHARATRAS.NS',
'BHARATWIRE.NS',
'BHARTIARTL.NS',
'BHEL.NS',
'BHUSANSTL.NS',
'BIGBLOC.NS',
'BIL.NS',
'BILENERGY.NS',
'BILPOWER.NS',
'BINANIIND.NS',
'BINDALAGRO.NS',
'BIOCON.NS',
'BIOFILCHEM.NS',
'BIRLACABLE.NS',
'BIRLACORPN.NS',
'BIRLAMONEY.NS',
'BKMINDST.NS',
'BLBLIMITED.NS',
'BLISSGVS.NS',
'BLKASHYAP.NS',
'BLS.NS',
'BLUEBLENDS.NS',
'BLUECOAST.NS',
'BLUEDART.NS',
'BLUESTARCO.NS',
'BODALCHEM.NS',
'BOHRA.NS',
'BOMDYEING.NS',
'BOSCHLTD.NS',
'BPCL.NS',
'BPL.NS',
'BRFL.NS',
'BRIGADE.NS',
'BRITANNIA.NS',
'BRNL.NS',
'BROOKS.NS',
'BSE.NS',
'BSELINFRA.NS',
'BSL.NS',
'BSLGOLDETF.NS',
'BSLIMITED.NS',
'BSLNIFTY.NS',
'BURNPUR.NS',
'BUTTERFLY.NS',
'BVCL.NS',
'BYKE.NS',
'CADILAHC.NS',
'CADSYS.NS',
'CALSOFT.NS',
'CAMLINFINE.NS',
'CANBK.NS',
'CANDC.NS',
'CANFINHOME.NS',
'CANTABIL.NS',
'CAPACITE.NS',
'CAPF.NS',
'CAPLIPOINT.NS',
'CAPTRUST.NS',
'CARBORUNIV.NS',
'CAREERP.NS',
'CARERATING.NS',
'CASTEXTECH.NS',
'CASTROLIND.NS',
'CCCL.NS',
'CCHHL.NS',
'CCL.NS',
'CDSL.NS',
'CEATLTD.NS',
'CEBBCO.NS',
'CELEBRITY.NS',
'CELESTIAL.NS',
'CENTENKA.NS',
'CENTEXT.NS',
'CENTRALBK.NS',
'CENTUM.NS',
'CENTURYPLY.NS',
'CENTURYTEX.NS',
'CERA.NS',
'CEREBRAINT.NS',
'CESC.NS',
'CGCL.NS',
'CGPOWER.NS',
'CHAMBLFERT.NS',
'CHENNPETRO.NS',
'CHOLAFIN.NS',
'CHROMATIC.NS',
'CIGNITITEC.NS',
'CIMMCO.NS',
'CINELINE.NS',
'CINEVISTA.NS',
'CIPLA.NS',
'CLEDUCATE.NS',
'CLNINDIA.NS',
'CMICABLES.NS',
'CMMIPL.NS',
'CNOVAPETRO.NS',
'COALINDIA.NS',
'COCHINSHIP.NS',
'COFFEEDAY.NS',
'COLPAL.NS',
'COMPINFO.NS',
'COMPUSOFT.NS',
'CONCOR.NS',
'CONSOFINVT.NS',
'CONTROLPR.NS',
'CORALFINAC.NS',
'CORDSCABLE.NS',
'COROMANDEL.NS',
'CORPBANK.NS',
'COSMOFILMS.NS',
'COUNCODOS.NS',
'COX&KINGS.NS',
'CPSEETF.NS',
'CREATIVE.NS',
'CREATIVEYE.NS',
'CREST.NS',
'CRISIL.NS',
'CRMFGETF.NS',
'CROMPTON.NS',
'CTE.NS',
'CUB.NS',
'CUBEXTUB.NS',
'CUMMINSIND.NS',
'CUPID.NS',
'CYBERMEDIA.NS',
'CYBERTECH.NS',
'CYIENT.NS',
'DAAWAT.NS',
'DABUR.NS',
'DALMIABHA.NS',
'DALMIASUG.NS',
'DAMODARIND.NS',
'DATAMATICS.NS',
'DBCORP.NS',
'DBL.NS',
'DBREALTY.NS',
'DCAL.NS',
'DCBBANK.NS',
'DCM.NS',
'DCMSHRIRAM.NS',
'DCW.NS',
'DECCANCE.NS',
'DEEPAKFERT.NS',
'DEEPAKNTR.NS',
'DEEPIND.NS',
'DELTACORP.NS',
'DELTAMAGNT.NS',
'DEN.NS',
'DENABANK.NS',
'DENORA.NS',
'DEVIT.NS',
'DFMFOODS.NS',
'DHAMPURSUG.NS',
'DHANBANK.NS',
'DHANUKA.NS',
'DHARSUGAR.NS',
'DHFL.NS',
'DHUNINV.NS',
'DIAMONDYD.NS',
'DIAPOWER.NS',
'DICIND.NS',
'DIGJAMLTD.NS',
'DISHTV.NS',
'DIVISLAB.NS',
'DIXON.NS',
'DLF.NS',
'DLINKINDIA.NS',
'DMART.NS',
'DOLLAR.NS',
'DOLPHINOFF.NS',
'DONEAR.NS',
'DPABHUSHAN.NS',
'DPL.NS',
'DPSCLTD.NS',
'DPWIRES.NS',
'DQE.NS',
'DREDGECORP.NS',
'DRREDDY.NS',
'DSKULKARNI.NS',
'DSSL.NS',
'DTIL.NS',
'DUCON.NS',
'DWARKESH.NS',
'DYNAMATECH.NS',
'DYNPRO.NS',
'EASTSILK.NS',
'EASUNREYRL.NS',
'ECEIND.NS',
'ECLERX.NS',
'ECLFINANCE.NS',
'EDELWEISS.NS',
'EDL.NS',
'EDUCOMP.NS',
'EHFLNCD.NS',
'EICHERMOT.NS',
'EIDPARRY.NS',
'EIFFL.NS',
'EIHAHOTELS.NS',
'EIHOTEL.NS',
'EIMCOELECO.NS',
'EKC.NS',
'ELAND.NS',
'ELECON.NS',
'ELECTCAST.NS',
'ELECTHERM.NS',
'ELGIEQUIP.NS',
'ELGIRUBCO.NS',
'EMAMIINFRA.NS',
'EMAMILTD.NS',
'EMCO.NS',
'EMKAY.NS',
'EMKAYTOOLS.NS',
'EMMBI.NS',
'ENDURANCE.NS',
'ENERGYDEV.NS',
'ENGINERSIN.NS',
'ENIL.NS',
'EON.NS',
'EQ30.NS',
'EQUITAS.NS',
'ERIS.NS',
'EROSMEDIA.NS',
'ESABINDIA.NS',
'ESCORTS.NS',
'ESL.NS',
'ESSARSHPNG.NS',
'ESSDEE.NS',
'ESSELPACK.NS',
'ESTER.NS',
'EUROCERA.NS',
'EUROMULTI.NS',
'EUROTEXIND.NS',
'EVEREADY.NS',
'EVERESTIND.NS',
'EXCEL.NS',
'EXCELCROP.NS',
'EXCELINDUS.NS',
'EXIDEIND.NS',
'FACT.NS',
'FAIRCHEM.NS',
'FCL.NS',
'FCONSUMER.NS',
'FDC.NS',
'FEDDERELEC.NS',
'FEDERALBNK.NS',
'FEL.NS',
'FELDVR.NS',
'FIEMIND.NS',
'FILATEX.NS',
'FINCABLES.NS',
'FINPIPE.NS',
'FLEXITUFF.NS',
'FLFL.NS',
'FMGOETZE.NS',
'FMNL.NS',
'FOCUS.NS',
'FORGE.NS',
'FORTIS.NS',
'FORTUNEFIN.NS',
'FOSECOIND.NS',
'FOURTHDIM.NS',
'FRETAIL.NS',
'FSL.NS',
'GABRIEL.NS',
'GAEL.NS',
'GAIL.NS',
'GAL.NS',
'GAMMNINFRA.NS',
'GAMMONIND.NS',
'GANDHITUBE.NS',
'GANECOS.NS',
'GANESHHOUC.NS',
'GANGESSECU.NS',
'GARDENSILK.NS',
'GARWALLROP.NS',
'GATI.NS',
'GAYAPROJ.NS',
'GDL.NS',
'GEECEE.NS',
'GEEKAYWIRE.NS',
'GEMINI.NS',
'GENESYS.NS',
'GENUSPAPER.NS',
'GENUSPOWER.NS',
'GEOJITFSL.NS',
'GEPIL.NS',
'GESHIP.NS',
'GET&D.NS',
'GHCL.NS',
'GICHSGFIN.NS',
'GICRE.NS',
'GILLANDERS.NS',
'GILLETTE.NS',
'GINNIFILA.NS',
'GIPCL.NS',
'GIRRESORTS.NS',
'GITANJALI.NS',
'GKWLIMITED.NS',
'GLAXO.NS',
'GLENMARK.NS',
'GLOBAL.NS',
'GLOBALVECT.NS',
'GLOBOFFS.NS',
'GLOBUSSPR.NS',
'GMBREW.NS',
'GMDCLTD.NS',
'GMRINFRA.NS',
'GNA.NS',
'GNFC.NS',
'GOACARBON.NS',
'GOCLCORP.NS',
'GODFRYPHLP.NS',
'GODREJAGRO.NS',
'GODREJCP.NS',
'GODREJIND.NS',
'GODREJPROP.NS',
'GOENKA.NS',
'GOKEX.NS',
'GOKUL.NS',
'GOKULAGRO.NS',
'GOLDBEES.NS',
'GOLDENTOBC.NS',
'GOLDIAM.NS',
'GOLDINFRA.NS',
'GOLDIWIN.NS',
'GOLDSHARE.NS',
'GOLDSTAR.NS',
'GOLDTECH.NS',
'GOODLUCK.NS',
'GPIL.NS',
'GPPL.NS',
'GPTINFRA.NS',
'GRANULES.NS',
'GRAPHITE.NS',
'GRASIM.NS',
'GRAVITA.NS',
'GREAVESCOT.NS',
'GREENLAM.NS',
'GREENPLY.NS',
'GREENPOWER.NS',
'GRINDWELL.NS',
'GROBTEA.NS',
'GRPLTD.NS',
'GRUH.NS',
'GSCLCEMENT.NS',
'GSFC.NS',
'GSKCONS.NS',
'GSPL.NS',
'GSS.NS',
'GTL.NS',
'GTLINFRA.NS',
'GTNIND.NS',
'GTNTEX.NS',
'GTPL.NS',
'GUFICBIO.NS',
'GUJALKALI.NS',
'GUJAPOLLO.NS',
'GUJFLUORO.NS',
'GUJGASLTD.NS',
'GUJNRECOKE.NS',
'GUJNREDVR.NS',
'GULFOILLUB.NS',
'GULFPETRO.NS',
'GULPOLY.NS',
'GVKPIL.NS',
'HANUNG.NS',
'HARITASEAT.NS',
'HARRMALAYA.NS',
'HATHWAY.NS',
'HATSUN.NS',
'HAVELLS.NS',
'HBLPOWER.NS',
'HBSTOCK.NS',
'HCC.NS',
'HCG.NS',
'HCL-INSYS.NS',
'HCLTECH.NS',
'HDFC.NS',
'HDFCBANK.NS',
'HDFCLIFE.NS',
'HDFCMFGETF.NS',
'HDFCNIFETF.NS',
'HDFCSENETF.NS',
'HDIL.NS',
'HECPROJECT.NS',
'HEG.NS',
'HEIDELBERG.NS',
'HERCULES.NS',
'HERITGFOOD.NS',
'HEROMOTOCO.NS',
'HESTERBIO.NS',
'HEXATRADEX.NS',
'HEXAWARE.NS',
'HFCL.NS',
'HGS.NS',
'HIGHGROUND.NS',
'HIKAL.NS',
'HIL.NS',
'HILTON.NS',
'HIMATSEIDE.NS',
'HINDALCO.NS',
'HINDCOMPOS.NS',
'HINDCOPPER.NS',
'HINDDORROL.NS',
'HINDMOTORS.NS',
'HINDNATGLS.NS',
'HINDOILEXP.NS',
'HINDPETRO.NS',
'HINDUJAVEN.NS',
'HINDUNILVR.NS',
'HINDZINC.NS',
'HIRECT.NS',
'HISARMETAL.NS',
'HITECH.NS',
'HITECHCORP.NS',
'HITECHGEAR.NS',
'HMT.NS',
'HMVL.NS',
'HONAUT.NS',
'HONDAPOWER.NS',
'HOTELEELA.NS',
'HOVS.NS',
'HPL.NS',
'HSCL.NS',
'HSIL.NS',
'HTMEDIA.NS',
'HUBTOWN.NS',
'HUDCO.NS',
'IBREALEST.NS',
'IBULHSGFIN.NS',
'IBVENTURES.NS',
'ICICIBANK.NS',
'ICICIGI.NS',
'ICICIPRULI.NS',
'ICIL.NS',
'ICRA.NS',
'ICSA.NS',
'IDBI.NS',
'IDBIGOLD.NS',
'IDEA.NS',
'IDFC.NS',
'IDFCBANK.NS',
'IDFNIFTYET.NS',
'IEX.NS',
'IFBAGRO.NS',
'IFBIND.NS',
'IFCI.NS',
'IFGLEXPOR.NS',
'IGARASHI.NS',
'IGL.NS',
'IGPL.NS',
'IIFCL.NS',
'IIFL.NS',
'IIFLFIN.NS',
'IIHFL.NS',
'IITL.NS',
'IL&FSENGG.NS',
'IL&FSTRANS.NS',
'IMFA.NS',
'IMPAL.NS',
'INDBANK.NS',
'INDHOTEL.NS',
'INDIACEM.NS',
'INDIAGLYCO.NS',
'INDIANB.NS',
'INDIANCARD.NS',
'INDIANHUME.NS',
'INDIGO.NS',
'INDIGRID.NS',
'INDLMETER.NS',
'INDNIPPON.NS',
'INDOCO.NS',
'INDORAMA.NS',
'INDOSOLAR.NS',
'INDOTECH.NS',
'INDOTHAI.NS',
'INDOWIND.NS',
'INDRAMEDCO.NS',
'INDSWFTLAB.NS',
'INDSWFTLTD.NS',
'INDTERRAIN.NS',
'INDUSINDBK.NS',
'INEOSSTYRO.NS',
'INFIBEAM.NS',
'INFINITE.NS',
'INFOBEAN.NS',
'INFRABEES.NS',
'INFRATEL.NS',
'INFY.NS',
'INGERRAND.NS',
'INNOVATIVE.NS',
'INOXLEISUR.NS',
'INOXWIND.NS',
'INSECTICID.NS',
'INTEGRA.NS',
'INTELLECT.NS',
'INTENTECH.NS',
'INVENTURE.NS',
'IOB.NS',
'IOC.NS',
'IOLCP.NS',
'IPAPPM.NS',
'IPCALAB.NS',
'IRB.NS',
'IRBINVIT.NS',
'IREDA.NS',
'IRFC.NS',
'ISFT.NS',
'ISMTLTD.NS',
'ITC.NS',
'ITDC.NS',
'ITDCEM.NS',
'ITI.NS',
'IVC.NS',
'IVP.NS',
'IVRCLINFRA.NS',
'IVZINGOLD.NS',
'IZMO.NS',
'J&KBANK.NS',
'JAGRAN.NS',
'JAGSNPHARM.NS',
'JAIBALAJI.NS',
'JAICORPLTD.NS',
'JAIHINDPRO.NS',
'JAINSTUDIO.NS',
'JALAN.NS',
'JAMNAAUTO.NS',
'JASH.NS',
'JAYAGROGN.NS',
'JAYBARMARU.NS',
'JAYNECOIND.NS',
'JAYSREETEA.NS',
'JBCHEPHARM.NS',
'JBFIND.NS',
'JBMA.NS',
'JCHAC.NS',
'JENSONICOL.NS',
'JETAIRWAYS.NS',
'JETKNIT.NS',
'JHS.NS',
'JINDALPHOT.NS',
'JINDALPOLY.NS',
'JINDALSAW.NS',
'JINDALSTEL.NS',
'JINDCOT.NS',
'JINDRILL.NS',
'JINDWORLD.NS',
'JISLDVREQS.NS',
'JISLJALEQS.NS',
'JITFINFRA.NS',
'JKCEMENT.NS',
'JKIL.NS',
'JKLAKSHMI.NS',
'JKPAPER.NS',
'JKTYRE.NS',
'JMA.NS',
'JMCPROJECT.NS',
'JMFINANCIL.NS',
'JMTAUTOLTD.NS',
'JOCIL.NS',
'JPASSOCIAT.NS',
'JPINFRATEC.NS',
'JPOLYINVST.NS',
'JPPOWER.NS',
'JSL.NS',
'JSLHISAR.NS',
'JSWENERGY.NS',
'JSWHL.NS',
'JSWSTEEL.NS',
'JUBILANT.NS',
'JUBLFOOD.NS',
'JUBLINDS.NS',
'JUNIORBEES.NS',
'JUSTDIAL.NS',
'JVLAGRO.NS',
'JYOTHYLAB.NS',
'JYOTISTRUC.NS',
'KABRAEXTRU.NS',
'KAJARIACER.NS',
'KAKATCEM.NS',
'KALPATPOWR.NS',
'KALYANIFRG.NS',
'KAMATHOTEL.NS',
'KAMDHENU.NS',
'KANANIIND.NS',
'KANORICHEM.NS',
'KANSAINER.NS',
'KARMAENG.NS',
'KARURVYSYA.NS',
'KAVVERITEL.NS',
'KAYA.NS',
'KCP.NS',
'KCPSUGIND.NS',
'KDDL.NS',
'KEC.NS',
'KECL.NS',
'KEERTI.NS',
'KEI.NS',
'KELLTONTEC.NS',
'KERNEX.NS',
'KESARENT.NS',
'KESORAMIND.NS',
'KEYCORPSER.NS',
'KGL.NS',
'KHADIM.NS',
'KHAITANLTD.NS',
'KHANDSE.NS',
'KICL.NS',
'KILITCH.NS',
'KINGFA.NS',
'KIOCL.NS',
'KIRIINDUS.NS',
'KIRLOSBROS.NS',
'KIRLOSENG.NS',
'KIRLOSIND.NS',
'KITEX.NS',
'KKCL.NS',
'KMSUGAR.NS',
'KNRCON.NS',
'KOHINOOR.NS',
'KOKUYOCMLN.NS',
'KOLTEPATIL.NS',
'KOPRAN.NS',
'KOTAKBANK.NS',
'KOTAKBKETF.NS',
'KOTAKGOLD.NS',
'KOTAKNIFTY.NS',
'KOTAKNV20.NS',
'KOTAKPSUBK.NS',
'KOTARISUG.NS',
'KOTHARIPET.NS',
'KOTHARIPRO.NS',
'KPIT.NS',
'KPRMILL.NS',
'KRBL.NS',
'KREBSBIO.NS',
'KRIDHANINF.NS',
'KRISHANA.NS',
'KSBPUMPS.NS',
'KSCL.NS',
'KSERASERA.NS',
'KSK.NS',
'KSL.NS',
'KTIL.NS',
'KTKBANK.NS',
'KWALITY.NS',
'L&TFH.NS',
'L&TFINANCE.NS',
'L&TINFRA.NS',
'LAKPRE.NS',
'LAKSHMIEFL.NS',
'LAKSHVILAS.NS',
'LALPATHLAB.NS',
'LAMBODHARA.NS',
'LAOPALA.NS',
'LASA.NS',
'LAURUSLABS.NS',
'LAXMIMACH.NS',
'LCCINFOTEC.NS',
'LEEL.NS',
'LEXUS.NS',
'LFIC.NS',
'LGBBROSLTD.NS',
'LIBAS.NS',
'LIBERTSHOE.NS',
'LICHSGFIN.NS',
'LICNETFGSC.NS',
'LICNETFN50.NS',
'LICNFNHGP.NS',
'LINCOLN.NS',
'LINCPEN.NS',
'LINDEINDIA.NS',
'LIQUIDBEES.NS',
'LITL.NS',
'LML.NS',
'LOKESHMACH.NS',
'LOTUSEYE.NS',
'LOVABLE.NS',
'LOWVOLIWIN.NS',
'LPDC.NS',
'LSIL.NS',
'LT.NS',
'LTI.NS',
'LTTS.NS',
'LUMAXIND.NS',
'LUMAXTECH.NS',
'LUPIN.NS',
'LUXIND.NS',
'LYCOS.NS',
'LYKALABS.NS',
'LYPSAGEMS.NS',
'M&M.NS',
'M&MFIN.NS',
'M100.NS',
'M15RD.NS',
'M50.NS',
'MAANALU.NS',
'MADHAV.NS',
'MADHUCON.NS',
'MADRASFERT.NS',
'MAGADSUGAR.NS',
'MAGMA.NS',
'MAGNUM.NS',
'MAHABANK.NS',
'MAHASTEEL.NS',
'MAHESHWARI.NS',
'MAHINDCIE.NS',
'MAHLIFE.NS',
'MAHLOG.NS',
'MAHSCOOTER.NS',
'MAHSEAMLES.NS',
'MAITHANALL.NS',
'MAJESCO.NS',
'MALUPAPER.NS',
'MANAKALUCO.NS',
'MANAKCOAT.NS',
'MANAKSIA.NS',
'MANAKSTEEL.NS',
'MANALIPETC.NS',
'MANAPPURAM.NS',
'MANAV.NS',
'MANDHANA.NS',
'MANGALAM.NS',
'MANGCHEFER.NS',
'MANGLMCEM.NS',
'MANGTIMBER.NS',
'MANINDS.NS',
'MANINFRA.NS',
'MANPASAND.NS',
'MANUGRAPH.NS',
'MARALOVER.NS',
'MARATHON.NS',
'MARICO.NS',
'MARKSANS.NS',
'MARUTI.NS',
'MASFIN.NS',
'MASTEK.NS',
'MATRIMONY.NS',
'MAWANASUG.NS',
'MAXINDIA.NS',
'MAXVIL.NS',
'MAYURUNIQ.NS',
'MAZDA.NS',
'MBAPL.NS',
'MBECL.NS',
'MBLINFRA.NS',
'MCDHOLDING.NS',
'MCDOWELL-N.NS',
'MCLEODRUSS.NS',
'MCX.NS',
'MEGASOFT.NS',
'MEGH.NS',
'MENONBE.NS',
'MEP.NS',
'MERCATOR.NS',
'MERCK.NS',
'METALFORGE.NS',
'METKORE.NS',
'MFSL.NS',
'MGL.NS',
'MHRIL.NS',
'MIC.NS',
'MIDCAPIWIN.NS',
'MILTON.NS',
'MINDACORP.NS',
'MINDAIND.NS',
'MINDTECK.NS',
'MINDTREE.NS',
'MIRCELECTR.NS',
'MIRZAINT.NS',
'MKPL.NS',
'MMFL.NS',
'MMTC.NS',
'MOHITIND.NS',
'MOHOTAMILL.NS',
'MOIL.NS',
'MOLDTECH.NS',
'MOLDTKPAC.NS',
'MOMAI.NS',
'MONNETISPA.NS',
'MONSANTO.NS',
'MONTECARLO.NS',
'MORARJEE.NS',
'MOREPENLAB.NS',
'MOSERBAER.NS',
'MOTHERSUMI.NS',
'MOTILALOFS.NS',
'MOTOGENFIN.NS',
'MPHASIS.NS',
'MPSLTD.NS',
'MRF.NS',
'MRPL.NS',
'MSPL.NS',
'MTEDUCARE.NS',
'MTNL.NS',
'MUKANDENGG.NS',
'MUKANDLTD.NS',
'MUKTAARTS.NS',
'MUNJALAU.NS',
'MUNJALSHOW.NS',
'MURUDCERA.NS',
'MUTHOOTCAP.NS',
'MUTHOOTFIN.NS',
'N100.NS',
'NABARD.NS',
'NACLIND.NS',
'NAGAFERT.NS',
'NAGAROIL.NS',
'NAGREEKCAP.NS',
'NAGREEKEXP.NS',
'NAHARCAP.NS',
'NAHARINDUS.NS',
'NAHARPOLY.NS',
'NAHARSPING.NS',
'NAKODA.NS',
'NANDANI.NS',
'NATCOPHARM.NS',
'NATHBIOGEN.NS',
'NATIONALUM.NS',
'NATNLSTEEL.NS',
'NAUKRI.NS',
'NAVINFLUOR.NS',
'NAVKARCORP.NS',
'NAVNETEDUL.NS',
'NBCC.NS',
'NBIFIN.NS',
'NBVENTURES.NS',
'NCC.NS',
'NCLIND.NS',
'NDGL.NS',
'NDL.NS',
'NDTV.NS',
'NECCLTD.NS',
'NECLIFE.NS',
'NELCAST.NS',
'NELCO.NS',
'NESCO.NS',
'NESTLEIND.NS',
'NETWORK18.NS',
'NEULANDLAB.NS',
'NEXTMEDIA.NS',
'NFL.NS',
'NH.NS',
'NHAI.NS',
'NHBTF2014.NS',
'NHBTF2023.NS',
'NHPC.NS',
'NIACL.NS',
'NIBL.NS',
'NIF100IWIN.NS',
'NIFTYBEES.NS',
'NIFTYEES.NS',
'NIFTYIWIN.NS',
'NIITLTD.NS',
'NIITTECH.NS',
'NILAINFRA.NS',
'NILKAMAL.NS',
'NIPPOBATRY.NS',
'NITCO.NS',
'NITESHEST.NS',
'NITINFIRE.NS',
'NITINSPIN.NS',
'NKIND.NS',
'NLCINDIA.NS',
'NMDC.NS',
'NOCIL.NS',
'NOIDATOLL.NS',
'NRAIL.NS',
'NRBBEARING.NS',
'NSIL.NS',
'NTL.NS',
'NTPC.NS',
'NUCLEUS.NS',
'NUTEK.NS',
'NV20IWIN.NS',
'OBEROIRLTY.NS',
'OCCL.NS',
'OCL.NS',
'OFSS.NS',
'OIL.NS',
'OILCOUNTUB.NS',
'OISL.NS',
'OMAXAUTO.NS',
'OMAXE.NS',
'OMKARCHEM.NS',
'OMMETALS.NS',
'ONELIFECAP.NS',
'ONGC.NS',
'ONMOBILE.NS',
'ONWARDTEC.NS',
'OPTIEMUS.NS',
'OPTOCIRCUI.NS',
'ORBTEXP.NS',
'ORCHIDPHAR.NS',
'ORICONENT.NS',
'ORIENTABRA.NS',
'ORIENTALTL.NS',
'ORIENTBANK.NS',
'ORIENTBELL.NS',
'ORIENTCEM.NS',
'ORIENTHOT.NS',
'ORIENTLTD.NS',
'ORIENTPPR.NS',
'ORIENTREF.NS',
'ORISSAMINE.NS',
'ORTEL.NS',
'ORTINLABSS.NS',
'PAEL.NS',
'PAGEIND.NS',
'PALASHSECU.NS',
'PALREDTEC.NS',
'PANACEABIO.NS',
'PANAMAPET.NS',
'PANORAMUNI.NS',
'PAPERPROD.NS',
'PARABDRUGS.NS',
'PARACABLES.NS',
'PARAGMILK.NS',
'PARSVNATH.NS',
'PASHUPATI.NS',
'PATELENG.NS',
'PATINTLOG.NS',
'PATSPINLTD.NS',
'PBAINFRA.NS',
'PCJEWELLER.NS',
'PDMJEPAPER.NS',
'PDPL.NS',
'PDSMFL.NS',
'PDUMJEIND.NS',
'PDUMJEPULP.NS',
'PEARLPOLY.NS',
'PEL.NS',
'PENIND.NS',
'PENINLAND.NS',
'PENPEBS.NS',
'PERFECT.NS',
'PERSISTENT.NS',
'PETRONENGG.NS',
'PETRONET.NS',
'PFC.NS',
'PFIZER.NS',
'PFOCUS.NS',
'PFS.NS',
'PGEL.NS',
'PGHH.NS',
'PGIL.NS',
'PHILIPCARB.NS',
'PHOENIXLTD.NS',
'PIDILITIND.NS',
'PIIND.NS',
'PILANIINVS.NS',
'PILITA.NS',
'PINCON.NS',
'PIONDIST.NS',
'PIONEEREMB.NS',
'PITTILAM.NS',
'PKTEA.NS',
'PLASTIBLEN.NS',
'PNB.NS',
'PNBGILTS.NS',
'PNBHOUSING.NS',
'PNC.NS',
'PNCINFRA.NS',
'POCHIRAJU.NS',
'PODDARHOUS.NS',
'PODDARMENT.NS',
'POKARNA.NS',
'POLARIS.NS',
'POLYMED.NS',
'POLYPLEX.NS',
'PONNIERODE.NS',
'POWERGRID.NS',
'POWERMECH.NS',
'PPAP.NS',
'PRABHAT.NS',
'PRADIP.NS',
'PRAENG.NS',
'PRAJIND.NS',
'PRAKASH.NS',
'PRAKASHCON.NS',
'PRATIBHA.NS',
'PRECAM.NS',
'PRECOT.NS',
'PRECWIRE.NS',
'PREMEXPLN.NS',
'PREMIER.NS',
'PREMIERPOL.NS',
'PRESSMN.NS',
'PRESTIGE.NS',
'PRICOLLTD.NS',
'PRIMESECU.NS',
'PRISMCEM.NS',
'PROVOGE.NS',
'PROZONINTU.NS',
'PSB.NS',
'PSL.NS',
'PSPPROJECT.NS',
'PSUBNKBEES.NS',
'PTC.NS',
'PTL.NS',
'PULZ.NS',
'PUNJABCHEM.NS',
'PUNJLLOYD.NS',
'PURVA.NS',
'PUSHPREALM.NS',
'PVP.NS',
'PVR.NS',
'QGOLDHALF.NS',
'QUESS.NS',
'QUICKHEAL.NS',
'QUINTEGRA.NS',
'RADAAN.NS',
'RADICO.NS',
'RADIOCITY.NS',
'RAIN.NS',
'RAINBOWPAP.NS',
'RAJESHEXPO.NS',
'RAJOIL.NS',
'RAJRAYON.NS',
'RAJSREESUG.NS',
'RAJTV.NS',
'RALLIS.NS',
'RAMANEWS.NS',
'RAMASTEEL.NS',
'RAMCOCEM.NS',
'RAMCOIND.NS',
'RAMCOSYS.NS',
'RAMKY.NS',
'RAMSARUP.NS',
'RANASUG.NS',
'RANEENGINE.NS',
'RANEHOLDIN.NS',
'RATNAMANI.NS',
'RAYMOND.NS',
'RBL.NS',
'RBLBANK.NS',
'RCF.NS',
'RCOM.NS',
'RECLTD.NS',
'REDINGTON.NS',
'REFEX.NS',
'REGENCERAM.NS',
'RELAXO.NS',
'RELCAPITAL.NS',
'RELCNX100.NS',
'RELCONS.NS',
'RELDIVOPP.NS',
'RELIABLE.NS',
'RELIANCE.NS',
'RELIFIN.NS',
'RELIGARE.NS',
'RELINFRA.NS',
'RELNV20.NS',
'REMSONSIND.NS',
'RENUKA.NS',
'REPCOHOME.NS',
'REPRO.NS',
'RESPONIND.NS',
'REVATHI.NS',
'RHFL.NS',
'RICOAUTO.NS',
'RIIL.NS',
'RJL.NS',
'RKDL.NS',
'RKEC.NS',
'RKFORGE.NS',
'RMCL.NS',
'RMDRIP.NS',
'RML.NS',
'RNAM.NS',
'RNAVAL.NS',
'ROHLTD.NS',
'ROLLT.NS',
'ROLTA.NS',
'ROSSELLIND.NS',
'RPGLIFE.NS',
'RPOWER.NS',
'RPPINFRA.NS',
'RRSLGETF.NS',
'RSSOFTWARE.NS',
'RSWM.NS',
'RSYSTEMS.NS',
'RTNINFRA.NS',
'RTNPOWER.NS',
'RUBYMILLS.NS',
'RUCHINFRA.NS',
'RUCHIRA.NS',
'RUCHISOYA.NS',
'RUPA.NS',
'RUSHIL.NS',
'SABEVENTS.NS',
'SABTN.NS',
'SADBHAV.NS',
'SADBHIN.NS',
'SAGARDEEP.NS',
'SAGCEM.NS',
'SAIL.NS',
'SAKHTISUG.NS',
'SAKSOFT.NS',
'SAKUMA.NS',
'SALASAR.NS',
'SALONA.NS',
'SALORAINTL.NS',
'SALSTEEL.NS',
'SALZERELEC.NS',
'SAMBHAAV.NS',
'SAMTEL.NS',
'SANCO.NS',
'SANDESH.NS',
'SANGAMIND.NS',
'SANGHIIND.NS',
'SANGHVIFOR.NS',
'SANGHVIMOV.NS',
'SANGINITA.NS',
'SANOFI.NS',
'SANWARIA.NS',
'SARDAEN.NS',
'SAREGAMA.NS',
'SARLAPOLY.NS',
'SASKEN.NS',
'SASTASUNDR.NS',
'SATHAISPAT.NS',
'SATIN.NS',
'SBILIFE.NS',
'SBIN.NS',
'SCAPDVR.NS',
'SCHAEFFLER.NS',
'SCHAND.NS',
'SCHNEIDER.NS',
'SCI.NS',
'SDBL.NS',
'SEAMECLTD.NS',
'SECURCRED.NS',
'SEINV.NS',
'SELAN.NS',
'SELMCL.NS',
'SENSEXIWIN.NS',
'SEPOWER.NS',
'SEQUENT.NS',
'SERVALL.NS',
'SERVOTECH.NS',
'SESHAPAPER.NS',
'SETCO.NS',
'SETF10GILT.NS',
'SETFGOLD.NS',
'SETFNIF50.NS',
'SETFNIFBK.NS',
'SETFNN50.NS',
'SEZAL.NS',
'SFL.NS',
'SGBAUG24.NS',
'SGBFEB24.NS',
'SGBJUL25.NS',
'SGBMAR25.NS',
'SGBMAY25.NS',
'SGBNOV23.NS',
'SGBNOV24.NS',
'SGBNOV25.NS',
'SGBOCT25.NS',
'SGBOCT25IV.NS',
'SGBOCT25V.NS',
'SGBSEP24.NS',
'SGL.NS',
'SHAHALLOYS.NS',
'SHAKTIPUMP.NS',
'SHALPAINTS.NS',
'SHANKARA.NS',
'SHANTI.NS',
'SHANTIGEAR.NS',
'SHARDACROP.NS',
'SHARDAMOTR.NS',
'SHARIABEES.NS',
'SHARONBIO.NS',
'SHEMAROO.NS',
'SHILPAMED.NS',
'SHILPI.NS',
'SHIRPUR-G.NS',
'SHIVAMAUTO.NS',
'SHK.NS',
'SHOPERSTOP.NS',
'SHREECEM.NS',
'SHREEPUSHK.NS',
'SHREERAMA.NS',
'SHRENIK.NS',
'SHREYANIND.NS',
'SHREYAS.NS',
'SHRIPISTON.NS',
'SHRIRAMCIT.NS',
'SHRIRAMEPC.NS',
'SHYAMCENT.NS',
'SHYAMTEL.NS',
'SICAGEN.NS',
'SICAL.NS',
'SIEMENS.NS',
'SIGNET.NS',
'SIIL.NS',
'SIL.NS',
'SILINV.NS',
'SIMBHALS.NS',
'SIMPLEX.NS',
'SIMPLEXINF.NS',
'SINTEX.NS',
'SIS.NS',
'SITASHREE.NS',
'SITINET.NS',
'SIYSIL.NS',
'SJVN.NS',
'SKFINDIA.NS',
'SKIL.NS',
'SKIPPER.NS',
'SKMEGGPROD.NS',
'SMARTLINK.NS',
'SMCSRVIRD.NS',
'SMCSRVIRG.NS',
'SMLISUZU.NS',
'SMPL.NS',
'SMSLIFE.NS',
'SMSPHARMA.NS',
'SNOWMAN.NS',
'SOBHA.NS',
'SOLARINDS.NS',
'SOMANYCERA.NS',
'SOMATEX.NS',
'SOMICONVEY.NS',
'SONASTEER.NS',
'SONATSOFTW.NS',
'SORILHOLD.NS',
'SORILINFRA.NS',
'SOTL.NS',
'SOUTHBANK.NS',
'SPAL.NS',
'SPARC.NS',
'SPECIALITY.NS',
'SPENTEX.NS',
'SPHEREGSL.NS',
'SPIC.NS',
'SPICEMOBI.NS',
'SPLIL.NS',
'SPMLINFRA.NS',
'SPTL.NS',
'SPYL.NS',
'SQSBFSI.NS',
'SREEL.NS',
'SREIBNPNCD.NS',
'SREINFRA.NS',
'SRF.NS',
'SRHHYPOLTD.NS',
'SRIPIPES.NS',
'SRIRAM.NS',
'SRSLTD.NS',
'SRTRANSFIN.NS',
'SSWL.NS',
'STAMPEDE.NS',
'STAN.NS',
'STAR.NS',
'STARCEMENT.NS',
'STARPAPER.NS',
'STCINDIA.NS',
'STEELCITY.NS',
'STEELXIND.NS',
'STEL.NS',
'STERLINBIO.NS',
'STERTOOLS.NS',
'STINDIA.NS',
'STRTECH.NS',
'SUBEX.NS',
'SUBROS.NS',
'SUDARSCHEM.NS',
'SUJANAUNI.NS',
'SUMEETINDS.NS',
'SUMMITSEC.NS',
'SUNCLAYLTD.NS',
'SUNDARAM.NS',
'SUNDARMFIN.NS',
'SUNDRMBRAK.NS',
'SUNDRMFAST.NS',
'SUNFLAG.NS',
'SUNILHITEC.NS',
'SUNPHARMA.NS',
'SUNTECK.NS',
'SUNTV.NS',
'SUPERHOUSE.NS',
'SUPERSPIN.NS',
'SUPPETRO.NS',
'SUPRAJIT.NS',
'SUPREMEIND.NS',
'SUPREMEINF.NS',
'SUPREMETEX.NS',
'SURANAIND.NS',
'SURANASOL.NS',
'SURANAT&P.NS',
'SUREVIN.NS',
'SURYALAXMI.NS',
'SURYAROSNI.NS',
'SUTLEJTEX.NS',
'SUVEN.NS',
'SUZLON.NS',
'SWANENERGY.NS',
'SWARAJENG.NS',
'SWELECTES.NS',
'SYMPHONY.NS',
'SYNCOM.NS',
'SYNDIBANK.NS',
'SYNGENE.NS',
'TAINWALCHM.NS',
'TAJGVK.NS',
'TAKE.NS',
'TALBROAUTO.NS',
'TALWALKARS.NS',
'TANLA.NS',
'TANTIACONS.NS',
'TARAJEWELS.NS',
'TARAPUR.NS',
'TARMAT.NS',
'TASTYBITE.NS',
'TATACHEM.NS',
'TATACOFFEE.NS',
'TATACOMM.NS',
'TATAELXSI.NS',
'TATAGLOBAL.NS',
'TATAINVEST.NS',
'TATAMETALI.NS',
'TATAMOTORS.NS',
'TATAMTRDVR.NS',
'TATAPOWER.NS',
'TATASPONGE.NS',
'TATASTEEL.NS',
'TBZ.NS',
'TCFSL.NS',
'TCI.NS',
'TCIDEVELOP.NS',
'TCIEXP.NS',
'TCIFINANCE.NS',
'TCPLPACK.NS',
'TCS.NS',
'TDPOWERSYS.NS',
'TEAMLEASE.NS',
'TECHIN.NS',
'TECHM.NS',
'TECHNO.NS',
'TECHNOFAB.NS',
'TEJASNET.NS',
'TERASOFT.NS',
'TEXINFRA.NS',
'TEXMOPIPES.NS',
'TEXRAIL.NS',
'TFCILTD.NS',
'TFL.NS',
'TGBHOTELS.NS',
'THANGAMAYL.NS',
'THEJO.NS',
'THEMISMED.NS',
'THERMAX.NS',
'THIRUSUGAR.NS',
'THOMASCOOK.NS',
'THOMASCOTT.NS',
'THYROCARE.NS',
'TI.NS',
'TIDEWATER.NS',
'TIFIN.NS',
'TIIL.NS',
'TIINDIA.NS',
'TIJARIA.NS',
'TIL.NS',
'TIMESGTY.NS',
'TIMETECHNO.NS',
'TIMKEN.NS',
'TINPLATE.NS',
'TIPSINDLTD.NS',
'TIRUMALCHM.NS',
'TIRUPATI.NS',
'TITAN.NS',
'TMRVL.NS',
'TNPETRO.NS',
'TNPL.NS',
'TOKYOPLAST.NS',
'TORNTPHARM.NS',
'TORNTPOWER.NS',
'TOTAL.NS',
'TPLPLASTEH.NS',
'TRANSWIND.NS',
'TREEHOUSE.NS',
'TRENT.NS',
'TRF.NS',
'TRIDENT.NS',
'TRIGYN.NS',
'TRIL.NS',
'TRITURBINE.NS',
'TRIVENI.NS',
'TTKHLTCARE.NS',
'TTKPRESTIG.NS',
'TTL.NS',
'TTML.NS',
'TULSI.NS',
'TV18BRDCST.NS',
'TVSELECT.NS',
'TVSMOTOR.NS',
'TVSSRICHAK.NS',
'TVTODAY.NS',
'TVVISION.NS',
'TWL.NS',
'UBL.NS',
'UCALFUEL.NS',
'UCOBANK.NS',
'UFLEX.NS',
'UFO.NS',
'UGARSUGAR.NS',
'UJAAS.NS',
'UJJIVAN.NS',
'ULTRACEMCO.NS',
'UMANGDAIRY.NS',
'UMESLTD.NS',
'UNICHEMLAB.NS',
'UNIENTER.NS',
'UNIONBANK.NS',
'UNIPLY.NS',
'UNITECH.NS',
'UNITEDBNK.NS',
'UNITEDPOLY.NS',
'UNITEDTEA.NS',
'UNITY.NS',
'UNIVCABLES.NS',
'UPL.NS',
'URJA.NS',
'USHAMART.NS',
'USHERAGRO.NS',
'UTINEXT50.NS',
'UTINIFTETF.NS',
'UTISENSETF.NS',
'UTTAMSTL.NS',
'UTTAMSUGAR.NS',
'UVSL.NS',
'V2RETAIL.NS',
'VADILALIND.NS',
'VAIBHAVGBL.NS',
'VAISHALI.NS',
'VAKRANGEE.NS',
'VALUEIND.NS',
'VARDHACRLC.NS',
'VARDMNPOLY.NS',
'VASCONEQ.NS',
'VASWANI.NS',
'VBL.NS',
'VEDL.NS',
'VENKEYS.NS',
'VENUSREM.NS',
'VERTOZ.NS',
'VESUVIUS.NS',
'VETO.NS',
'VGUARD.NS',
'VHL.NS',
'VICEROY.NS',
'VIDEOIND.NS',
'VIDHIING.NS',
'VIJAYABANK.NS',
'VIJIFIN.NS',
'VIJSHAN.NS',
'VIKASECO.NS',
'VIMTALABS.NS',
'VINATIORGA.NS',
'VINDHYATEL.NS',
'VINYLINDIA.NS',
'VIPCLOTHNG.NS',
'VIPIND.NS',
'VIPULLTD.NS',
'VISAKAIND.NS',
'VISASTEEL.NS',
'VISHNU.NS',
'VIVIDHA.NS',
'VIVIMEDLAB.NS',
'VLSFINANCE.NS',
'VMART.NS',
'VOLTAMP.NS',
'VOLTAS.NS',
'VRLLOG.NS',
'VSCL.NS',
'VSSL.NS',
'VSTIND.NS',
'VSTTILLERS.NS',
'VTL.NS',
'WABAG.NS',
'WABCOINDIA.NS',
'WALCHANNAG.NS',
'WANBURY.NS',
'WEBELSOLAR.NS',
'WEIZFOREX.NS',
'WEIZMANIND.NS',
'WELCORP.NS',
'WELENT.NS',
'WELINV.NS',
'WELSPUNIND.NS',
'WENDT.NS',
'WHEELS.NS',
'WHIRLPOOL.NS',
'WILLAMAGOR.NS',
'WINDMACHIN.NS',
'WINSOME.NS',
'WIPL.NS',
'WIPRO.NS',
'WOCKPHARMA.NS',
'WONDERLA.NS',
'WORTH.NS',
'WSI.NS',
'WSTCSTPAPR.NS',
'XCHANGING.NS',
'XLENERGY.NS',
'XPROINDIA.NS',
'YESBANK.NS',
'ZANDUREALT.NS',
'ZEEL.NS',
'ZEELEARN.NS',
'ZEEMEDIA.NS',
'ZENITHEXPO.NS',
'ZENSARTECH.NS',
'ZENTEC.NS',
'ZICOM.NS',
'ZODIACLOTH.NS',
'ZODJRDMKJ.NS',
'ZOTA.NS',
'ZUARI.NS',
'ZUARIGLOB.NS',
'ZYDUSWELL.NS',
'ZYLOG.NS']

data_file_not_found_ctr = 0

records_not_enough_ctr = 0

no_models_ctr = 0

prediction_error_ctr = 0

prediction_success_ctr = 0

stock_processed_ctr = 0

import datetime
import logging
current_datetime = datetime.datetime.today()
current_date = str(current_datetime).split(' ')
log_filename = str('C:\\Users\EMBA\\Documents\\Data\\Scheduled Jobs\\NSE\\Logs\\Prediction_Process_') +current_date[0] +str('.log')
logging.basicConfig(filename=log_filename,level=logging.INFO,format='%(asctime)s %(message)s')

logging.info('Starting the process - %s', current_datetime)
print (current_datetime)

data_folder = 'C:\\Users\\EMBA\\Documents\\Data\\NSE_Data\\Data\\Featurized\\'
simulation_folder = 'C:\\Users\\EMBA\\Documents\\Data\\NSE_Data\\Data\\Simulation\\'
last_processed_path = 'C:\\Users\\EMBA\\Documents\\Data\\NSE_Data\\Data\\Simulation\\' +str('Last_Prediction.csv')
last_processed_file = pd.read_csv(last_processed_path)
last_processed_date = last_processed_file['Last_Processed_Bday'].iloc[0]

last_processed_model = 'C:\\Users\\EMBA\\Documents\\Data\\NSE_Data\\Model\\' +str('Last_Model.csv')
last_processed_mfile = pd.read_csv(last_processed_model)
last_processed_mdate = last_processed_mfile['Last_Processed_Bday'].iloc[0]

last_processed_datetime = datetime.datetime.strptime(last_processed_date,'%m/%d/%Y').date()
last_processed_mdatetime = datetime.datetime.strptime(last_processed_mdate,'%m/%d/%Y').date()

model_folder = 'C:\\Users\\EMBA\\Documents\\Data\\NSE_Data\\Model\\' +str(last_processed_mdatetime) + '\\'
next_process_datetime = last_processed_datetime + BDay(1)
#next_process_date = datetime.datetime.strptime(str(next_process_datetime),'%m/%d/%Y').date()
next_process_date_file = str(next_process_datetime).split(' ')
next_process_date = next_process_date_file[0].split('-')
next_process_date = next_process_date[1] +str('/') +next_process_date[2] +str('/') + next_process_date[0]

new_row = {'Stock':['dummy'],'Date':next_process_date,'Prediction':['NA'],'Action':[0],'Probability':[0.0]}
forecast = pd.DataFrame(data=new_row,index=None,columns=('Stock','Date','Prediction', 'Action', 'Probability'))

model_performance_file_path = model_folder + str('Model_Performance_') +str(last_processed_mdatetime) +str('.csv')
model_performance = pd.read_csv(model_performance_file_path)

#y = (model_performance['Accuracy'] > model_performance['Majority_Class']) and (model_performance['Precision'] > model_performance['Recall'])
#model_performance['Predict'] = model_performance['Accuracy'].apply(lambda x: y)
model_performance = model_performance[model_performance['Predict'] == 'Yes']
#print (model_performance)

def normalize_features(features):
    from sklearn.preprocessing import normalize
    features = normalize(features,axis=0)
    features = normalize(features,axis=1)
    return features
for stock in stocks:
#stock = 'NSE.NS'
#if stock == 'NSE.NS':
    #file_name = str(stock) + str(end_date) +str('.csv')
    #file_name = str(stock) + str('2017-11-24') +str('.csv')
    file_name = str(stock) +str('.csv')
    data_file_path = data_folder +  file_name
    #print (data_file_path)
    stock_processed_ctr += 1    
    try:
        stock_data = pd.read_csv(data_file_path,dtype={'Date':str,'Open':float,'High':float,'Low':float,'Close':float,'Adj Close':float,
                                        'Volume':float})
        find_row = stock_data[stock_data['Date'] == next_process_date]
        skip = False
    except:
        skip = True
        logging.info('Data file not found for - %s', stock)
        data_file_not_found_ctr += 1
    
    if skip == False:
        stock_data = stock_data.replace([np.inf, -np.inf], np.nan)
        stock_data.fillna(0,inplace=True)
        attr_cols = stock_data.columns
        feature_cols = []
        static_cols = []
        signal_cols = []
        for i in attr_cols:
            attr_list=[]
            attr_list = i.split('_')
            if 'RBC' in attr_list or 'DBC' in attr_list or 'RBCV'in attr_list or 'DBCV' in attr_list or 'Add' in attr_list:
                feature_cols.append(i)
            if 'Signal' in attr_list:
                signal_cols.append(i)
        if stock == 'NSE.NS':
            feature_cols.append('P/E')
            feature_cols.append('P/B')
            feature_cols.append('Div Yield')

        features = stock_data[feature_cols]
        feature_cols.append('Date')
        feature_cols.append('Open')
        feature_cols.append('Close')
        feature_cols.append('Volume')   
        feature_cols.append('% Change')
        #stock_data = stock_data[feature_cols]
        #stock_data = stock_data[200:]
        #features = features[200:]
        #print (features)
        if features.shape[0] > 400:
            features = normalize_features(features)
        else:
            skip = True
            logging.info('Sufficient records not available for - %s', stock)
            records_not_enough_ctr += 1
        #print ('success')
    
    #print ('skip = ' +str(skip))
    
    if skip == False:
        #print ('finding models for ' +str(stock))
        stock_models = model_performance[model_performance['Stock'] == stock]
        if stock_models.shape[0] < 1:
            logging.info('No models found for stock - %s', stock)
            no_models_ctr += 1
            skip = True

    if skip == False:
        for i in range(stock_models.shape[0]):
            #print ('models found for stock ' +str(stock))
            t_signal = stock_models['Prediction'].iloc[i]
            penalty = stock_models['Penalty'].iloc[i]
            maxiter = stock_models['Max_Iter'].iloc[i]
            tolerance = stock_models['Tolerance'].iloc[i]
            model_name = stock +str(t_signal) +str('_') +str(penalty) +str('_') + str (maxiter) +str('_') + str(tolerance) +str('.sav')
            model_file_path = model_folder + model_name
            #print (model_file_path)
            try:
                model = pickle.load(open(model_file_path, 'rb'))
                #print (model)
                #X = features.reshape(-1,features.shape[1])
                #print (X)
                pred_col = t_signal + str('_') + str('Pred') +str('_') +str(penalty) +str('_') +str (maxiter) +str('_') + str(tolerance) +str('_') + str(next_process_date_file[0]) 
                pred_signal_prob0 = t_signal +str('_') +str(penalty) +str('_') +str (maxiter) +str('_') + str(tolerance) +str('_') +str('Prob_0') + str('_') + str(next_process_date_file[0])
                pred_signal_prob1 = t_signal +str('_') +str(penalty) +str('_') +str (maxiter) +str('_') + str(tolerance) +str('_') +str('Prob_1') + str('_') + str(next_process_date_file[0])
                stock_data[pred_col] = predicted_target = model.predict(features)
                #print ('prediction successful ' +str(stock))
                #x_pred_col = t_signal + str('_') + str('Pred') +str('_') + str(end_date) 
                #x_pred_signal_prob0 = t_signal +str('_') +str('Prob_0') + str('_') + str(end_date)
                #x_pred_signal_prob1 = t_signal + str('_') +str('Prob_1') + str('_') + str(end_date)
                #del stock_data[x_pred_col]
                #del stock_data[x_pred_signal_prob0]
                #del stock_data[x_pred_signal_prob1]
                #print (predicted_target)
                stock_data[pred_signal_prob0] = [item[0] for item in model.predict_proba(features)]
                #print (stock_data[pred_signal_prob0])
                stock_data[pred_signal_prob1] = [item[1] for item in model.predict_proba(features)]
                #print (stock_data[pred_signal_prob1])
                stock_data['Date'] = stock_data['Date'].astype('str')
                find_row = stock_data[stock_data['Date'] == next_process_date_file[0]]
                if find_row.shape[0] == 1:
                    if find_row[pred_col].iloc[0] == 0:
                    #prob = model.predict_proba(features)[-1][0]
                        #print ('Predicted 0')
                        prob = find_row[pred_signal_prob0].iloc[0]
                        #print ('prob ' +str(prob))
                    else:
                        #prob = model.predict_proba(features)[-1][1]
                        #print ('Predicted 1')
                        prob = find_row[pred_signal_prob1].iloc[0]
                        #print ('prob ' +str(prob))
                    #print ('prob ' +str(prob))
                    #new_row = {'Stock':stock,'Date':next_process_date,'Prediction':(str(t_signal) +str('_') +str(penalty) +str('_') + str (maxiter) +str('_') + str(tolerance)),'Action':predicted_target[-1],'Probability':prob}
                    new_row = {'Stock':stock,'Date':next_process_date,'Prediction':(str(t_signal) +str('_') +str(penalty) +str('_') + str (maxiter) +str('_') + str(tolerance)),'Action':find_row[pred_col].iloc[0],'Probability':prob}
                    #print (new_row)
                    forecast = forecast.append(new_row,ignore_index=True)
                    prediction_success_ctr += 1
                    #print (forecast)
                    skip = False
                else:
                    skip = True
                    logging.info('Trade data not found for processing date - %s', stock)
                    i = stock_models.shape[0]
            except:
                skip = True
                logging.info('Error occured while predicting for - %s', stock)
                prediction_error_ctr += 1
        stock_data.to_csv(data_file_path,index=False)

target_folder = 'C:\\Users\\EMBA\\Documents\\Data\\NSE_Data\\Data\\Simulation\\'
file_name = 'NSE Stock Prediction_' +str(next_process_date_file[0]) + str('.csv')
target_file_path = target_folder + file_name
forecast.to_csv(target_file_path,index=False)
last_processed_file['Last_Processed_Bday'].iloc[0] = next_process_date
last_processed_file.to_csv(last_processed_path,index=False)
#print (next_process_date)
current_datetime = datetime.datetime.today()
logging.info('Stopping the process - ', current_datetime)
logging.info('******************************* Execution Summary ******************************')
logging.info('Total Number of Stocks processed - %s', stock_processed_ctr)
logging.info('Total Numer of Models predicted for %s - %s', next_process_date, prediction_success_ctr)
logging.info('********************************************************************************')
logging.info('******************************* Failure summary ********************************')
logging.info('Total Number of Stocks for which data file not found %s',data_file_not_found_ctr)
logging.info('Total Number of Stocks for which Enough Records were not available %s', records_not_enough_ctr)
logging.info('Total Number of Stocks for which Good Models were not available %s', no_models_ctr)
logging.info('Total Number of Models with prediction error %s', prediction_error_ctr)
logging.info('********************************************************************************')
