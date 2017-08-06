#include "TGeoManager.h"


void handle_node(TGeoNode* nextnode) {
  auto objarr =nextnode->GetNodes(); 
  if (objarr) {
  int s = objarr->GetSize();
  for (int i = 0; i < s; ++i) {
    TGeoNode* n = (TGeoNode *)objarr->At(i);
    
    if (n) {
  std::cout<<n->GetName()<<std::endl;
  //gGeoManager->cd(n->GetName());
  n->ls();
  std::cout<<*(gGeoManager->GetGLMatrix()->GetTranslation())<<"\t";
  std::cout<<*(gGeoManager->GetGLMatrix()->GetTranslation()+1)<<"\t";
  std::cout<<*(gGeoManager->GetGLMatrix()->GetTranslation()+2)<<std::endl;
    //std::cout<<*(n->GetMatrix()->GetTranslation())<<std::endl;
    //std::cout<<*(n->GetMatrix()->GetTranslation()+1)<<std::endl;
    //std::cout<<*(n->GetMatrix()->GetTranslation()+2)<<std::endl;
    //n->Draw("");
    handle_node(n);
    }
    
  }

}
    else{ 
  }
}


void loopgdml(){

  TGeoManager* geom = new TGeoManager();
  geom->Import("test.gdml");
  TGeoVolume* a = geom->GetTopVolume();
  TGeoNode* b = (TGeoNode*) a->GetNodes()->At(0);
  handle_node(b);


}
