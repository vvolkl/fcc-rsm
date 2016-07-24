#include "TGeoManager.h"

void visgdml () {
  TGeoManager* gman = new TGeoManager();
  gman->Import("test.gdml");
  gman->SetVisLevel(5);
  TGeoVolume* top = gman->GetTopVolume();
  top->Draw("ogl");
  gman->SetVisOption(0);
}
