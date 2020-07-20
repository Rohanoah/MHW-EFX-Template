# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 15:33:22 2020

@author: AsteriskAmpersand
"""



existingHashes = [
        "nEffect::ExternReference",
"nEffect::FakePlane",
"nEffect::TypeDummy",
"nEffect::RandomFix",
"nEffect::Transform2D",
"nEffect::TypeBillboard2D",
"nEffect::Blink",
"nEffect::LuminanceBleed",
"nEffect::EmitterShape2D",
"nEffect::Velocity2D",
"nEffect::Distortion",
"nMhEffect::MasterOnly",
"nEffect::TubeLight",
"nEffect::Shovel (find me an example and I'll map this one, already did .shvls)",
"nEffect::Layout",
"nEffect::FakeDoF",
"nEffect::RepeatArea",
"nEffect::LinkPartsVisible",
"nEffect::PtTrigger",
"nEffect::PathChain",
"nEffect::Homing",
"nEffect::EmitterShapeMesh",
"nEffect::SpawnByAngle",
"nEffect::CheckPureAttribute",
"nEffect::TonemapFilter",
"nEffect::ColorCorrectFilter",
"nEffect::Transform3D",
"nEffect::ParentOptions",
"nEffect::Spawn",
"nEffect::Life",
"nEffect::EmitterShape3D",
"nEffect::Velocity3D",
"nEffect::FadeByDepth",
"nEffect::TypeRibbonBlade",
"nEffect::TypeBillboard3D",
"nEffect::ScaleAnim",
"nEffect::UVSequence",
"nEffect::AlphaCorrection",
"nEffect::ShaderSettings",
"nEffect::RgbFire",
"nEffect::TypeMesh",
"nEffect::RotateAnim",
"nMhEffect::PlEmissive",
"nEffect::Guide",
"nEffect::TypeLightning",
"nMhEffect::ParentEmissive",
"nEffect::PtCollision",
"nMhEffect::PlSnow",
"nEffect::PtBehavior",
"nEffect::Material",
"nEffect::TypePlane",
"nEffect::RgbWater",
"nEffect::Turbulence",
"nEffect::FadeByEmitterAngle",
"nEffect::TypeRibbon",
"nEffect::Noise",
"nEffect::UVControl",
"nEffect::FadeByAngle",
"nEffect::EmitterBoundary",
"nEffect::PtLife",
"nEffect::StrainRibbon",
"nEffect::ScreenSpaceCollision",
"nEffect::RayCast",
"nEffect::SpawnByOcclusion",
"nEffect::FadeByOcclusion",
"nMhEffect::ParentSnow",
"nMhEffect::OtomoSnow",
"nEffect::ParentMaterial",
"nEffect::ExternTransform3D",
"nEffect::ExternTypeMesh",
"nMhEffect::ExternPlEmissive",
"nEffect::ExternPtBehavior",
"nEffect::ExternRgbWater",
"nEffect::ExternVelocity3D",
"nEffect::ExternEmitterShape3D",
"nMhEffect::ExternParentEmissive",
"nEffect::ExternSpawn",
"nEffect::ExternRgbFire",
"nEffect::ExternTypeRibbon",
"nEffect::ExternRotateAnim",
"nEffect::ExternTypeBillboard3D",
"nEffect::ExternScaleAnim",
"nEffect::ExternLife",
"nEffect::ExternUVSequence",
"nEffect::ExternTypePlane",
"nMhEffect::ExternPlSnow",
"nEffect::UnitBoundary",
"nEffect::RenderTarget",
"nEffect::LayoutBank",
        ]

effectHashes = [("nEffect::EffectAttrColorTbl",1690896576),
("nEffect::MhEffectDecalBehavior",1128324015),
("nEffect::MhEffectDecalBehavior::getTotalFireLifeFrame",1250245974),
("nEffect::MhEffectDecalBehavior::getTotalSmokeLifeFrame",409149100),
("nEffect::MhEffectDecalBehavior::getTotalSpecularLifeFrame",173467491),
("nEffect::MhEffectDecalBehavior::getTotalSheetLifeFrame",1969325070),
("nEffect::MhEffectDecalBehavior::getTotalGtoBLifeFrame",1296538020),
("nEffect::cCoordParameter",1892103853),
("nEffect::IEffectItem",19434345),
("nEffect::Item",1215086948),
("nEffect::DynamicRay",1708014292),
("nEffect::FlowmapSettings",1184613359),
("nEffect::EffectExecutor",1213896611),
("nEffect::TypeMesh",276670093),
("nEffect::EmitterShape2D",584030352),
("nEffect::ExternVelocity3D",351887441),
("nEffect::ExternEmitterShape3D",1880343637),
("nEffect::ExternRotateAnim",1879331968),
("nEffect::ExternScaleAnim",786529163),
("nEffect::ExternUVSequence",2097096908),
("nEffect::ExternFadeByAngle",1415485201),
("nEffect::ExternFadeByDepth",779931249),
("nEffect::ExternLife",1338793878),
("nEffect::ExternTransform3D",500644368),
("nEffect::ExternTypeBillboard3D",693979274),
("nEffect::ExternTypePlane",805496014),
("nEffect::ExternTypeRibbon",839790967),
("nEffect::ExternTypeMesh",1850314036),
("nEffect::ExternStrainRibbon",167781675),
("nEffect::ExternPtBehavior",1610366518),
("nEffect::ExternRgbFire",2069124466),
("nEffect::ExternRgbWater",482524730),
("nEffect::ExternUVControl",1243935109),
("nEffect::ExternTurbulence",777721399),
("nEffect::ExternSpawn",28559457),
("nEffect::ExternItem",1226458230),
("nEffect::BasicExternItem",1771113640),
("nEffect::ExternReference",351869514),
("nEffect::EffectEvent",1923506186),
("nEffect::EventBehaviorProperty",346395602),
("nEffect::DecalBehavior",657374606),
("nEffect::Variant",588732697),
("nEffect::LightBehavior",603167555),
("nEffect::PointLightBehavior",110612213),
("nEffect::SpotLightBehavior",804054309),
("nEffect::uEffectRadialBlurFilter",1183727815),
("nEffect::FilterBehavior",618247822),
("nEffect::RadialBlurFilterBehavior",1161774816),
("nEffect::Distortion",957228464),
("nEffect::RandomFix",674258598),
("nEffect::Life",1320868484),
("nEffect::StrainRibbon",1062052310),
("nEffect::EffectData",1135895459),
("nEffect::EmitterExecutor",2097355886),
("nEffect::Transform2D",428328940),
("nEffect::Transform3D",10286765),
("nEffect::ParentOptions",368199626),
("nEffect::LinkPartsVisible",812022019),
("nEffect::Spawn",1921765292),
("nEffect::SpawnByAngle",1916268445),
("nEffect::SpawnByOcclusion",1913890808),
("nEffect::TypeDummy",201720946),
("nEffect::TypeBillboard2D",1524169119),
("nEffect::TypeBillboard3D",1136904414),
("nEffect::TypePlane",37870541),
("nEffect::TypeMie3D",1771758423),
("nEffect::TypeRibbon",733291506),
("nEffect::TypeRibbonBlade",319363982),
("nEffect::Velocity2D",341394325),
("nEffect::Velocity3D",222458580),
("nEffect::UVControl",2020068998),
("nEffect::RotateAnim",1774142981),
("nEffect::ScaleAnim",480396424),
("nEffect::UVSequence",1698970185),
("nEffect::EmitterShape3D",1003792849),
("nEffect::EmitterShapeMesh",1111321825),
("nEffect::AlphaCorrection",61219887),
("nEffect::TypeLightning",1558046267),
("nEffect::ShaderSettings",1978267738),
("nEffect::TubeLight",252064274),
("nEffect::RayCast",275476317),
("nEffect::UnitBoundary",1413509420),
("nEffect::EmitterBoundary",873436648),
("nEffect::RenderTarget",2083659062),
("nEffect::PtLife",493311524),
("nEffect::PtBehavior",1179069619),
("nEffect::PlayEfx",1965813039),
("nEffect::Shovel",1240420851),
("nEffect::FadeByAngle",1226136492),
("nEffect::FadeByDepth",859243212),
("nEffect::FadeByOcclusion",64111316),
("nEffect::FadeByEmitterAngle",2116359897),
("nEffect::FakeDoF",212167510),
("nEffect::FakePlane",1257264016),
("nEffect::PlayEmitter",1152332069),
("nEffect::RgbFire",459578090),
("nEffect::RgbWater",1660327299),
("nEffect::Turbulence",937428146),
("nEffect::Material",1659025771),
("nEffect::ParentMaterial",638869640),
("nEffect::GroupItem",2043222009),
("nEffect::PtCollision",280719621),
("nEffect::ScreenSpaceCollision",697457224),
("nEffect::Noise",523015778),
("nEffect::Blink",1354601878),
("nEffect::PathChain",1217635032),
("nEffect::RepeatArea",842043995),
("nEffect::Homing",1535857470),
("nEffect::GpuPhysics",393634900),
("nEffect::PtTrigger",2115227124),
("nEffect::Layout",156539255),
("nEffect::LayoutBank",2050487542),
("nEffect::CheckPureAttribute",283684959),
("nEffect::EmitterShape3DOverrider",1105989980),
("nEffect::LuminanceBleed",71967929),
("nEffect::ColorCorrectFilter",1293936879),
("nEffect::TonemapFilter",845585410),
("nEffect::MemoItem",1484483739),
("nEffect::IItemPropertyInfo",716000960),
("nEffect::EffectDatabase::ItemPropertyInfo",997811050),
("nEffect::EffectDatabase",1987779161),
("nEffect::TimelineResource",610766284),
("nEffect::TimelineListResource",1650401859),
("nEffect::INode",881621517),
("nEffect::Node",1376259135),
("nEffect::Root",1099111713),
("nEffect::Group",256197774),
("nEffect::Emitter",668609413),
("nEffect::Action",1956806151),
("nEffect::Field",963659027),
("nEffect::Extern",242552826),
("nEffect::Node::getType",1929273712),
("nEffect::VelocityBase",261120345),
("nEffect::TypeBillboardBase",1590369728),
("nEffect::EffectGroupData",1608814288),
("nEffect::EffectGroup",617098856),
("nEffect::BoundaryBase",1100150108),
("nEffect::RenderTarget::Target",1478767196),
("nEffect::TexturePath",386986771),
("nEffect::TypeLightning::Branch",2120416030),
("nEffect::TypeRibbonBladeSection",19293690),
("nEffect::TubeLightSection",292704954),
("nEffect::EffectSettingPreset",712996915),
("nEffect::EffectTimeRedeemPreset",916096233),
("nEffect::Material::MaterialParam",312479394),
("nEffect::Material::MaterialNodeData",1851897063),
("nEffect::ShapeMeshHolder",738773001),
("nMhEffect::cEffectProviderCustomData::ActionElement",510816299),
("nMhEffect::cEffectProviderCustomData::UnitElement",1178760989),
("nMhEffect::cEffectProviderCustomData",1867843721),
("nMhEffect::OtomoSnow",180261702),
("nMhEffect::ParentSnow",215153612),
("nMhEffect::PlSnow",1267346617),
("nMhEffect::PlEmissiveManager",910471525),
("nMhEffect::MasterOnly",1616705008),
("nMhEffect::ParentEmissive",14579343),
("nMhEffect::PlEmissive",597394907),
("nMhEffect::ExternGuide",766474541),
("nMhEffect::ExternParentEmissive",705591903),
("nMhEffect::ExternParentSnow",74649634),
("nMhEffect::ExternPlEmissive",725249589),
("nMhEffect::ExternPlSnow",283026906),
("nMhEffect::ExternOtomoSnow",1181241355),
("nMhEffect::Guide::MoveType::AlwaysThrough",1168412664),
("nMhEffect::Guide::MoveType::SkipNear",889775412),
("nMhEffect::Guide::MoveType::OldType",594406925),
("nMhEffect::Guide",1123011591)]

w = []

existingHashes = set(existingHashes)
for (hname,hval) in effectHashes:
    if hname not in existingHashes:
        name = hname.replace("nEffect::","").replace("nMhEffect::","").replace("::","_").replace("\n","").replace("\r","")
        w.append((name,hval))
        print("""const int %s"""%name.upper().ljust(50) +
              """= %d; // %08X"""%(hval,hval))
print() 
for (hname,hval) in w:
    branch = """            else if (ReadInt() == %s      )
            %s      %s"""%(hname.upper(),hname,hname.lower())
    print(branch)
print()   
for (hname,hval) in w:
    print("""typedef struct{}%s;"""%(hname))