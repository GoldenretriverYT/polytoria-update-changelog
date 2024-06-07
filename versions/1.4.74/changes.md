# Changes
## DecalProxy
Inherits from: [DynamicInstanceProxy](#DynamicInstanceProxy)
- Property `ImageType` in `DecalProxy` changed type from `ImageType` to `Polytoria.Controllers.ImageType`
## DynamicInstanceProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Method `LookAt` changed parameters: 
  - Parameter `dynamicInstance` changed type from `DynamicInstance` to `Polytoria.Datamodel.DynamicInstance`
## EnvironmentProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Method `CreateExplosion` changed parameters: 
  - Parameter `func` changed type from `MoonSharp.Interpreter.DynValue` to `MoonSharp.Interpreter.DynValue`
- Method `Raycast` changed parameters: 
  - Parameter `ignoreList` changed type from `System.Collections.Generic.List`1[[Instance, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null]]` to `System.Collections.Generic.List`1[[Polytoria.Datamodel.Instance, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null]]`
- Method `RaycastAll` changed parameters: 
  - Parameter `ignoreList` changed type from `System.Collections.Generic.List`1[[Instance, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null]]` to `System.Collections.Generic.List`1[[Polytoria.Datamodel.Instance, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null]]`
- Method `OverlapSphere` changed parameters: 
  - Parameter `ignoreList` changed type from `System.Collections.Generic.List`1[[Instance, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null]]` to `System.Collections.Generic.List`1[[Polytoria.Datamodel.Instance, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null]]`
- Method `OverlapBox` changed parameters: 
  - Parameter `ignoreList` changed type from `System.Collections.Generic.List`1[[Instance, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null]]` to `System.Collections.Generic.List`1[[Polytoria.Datamodel.Instance, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null]]`
- Property `Skybox` in `EnvironmentProxy` changed type from `SkyboxPreset` to `Polytoria.Datamodel.SkyboxPreset`
## GameProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Property `Rendered` in `GameProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## InstanceProxy
Inherits from: [Object](#Object)
- Method `SetParent` changed parameters: 
  - Parameter `parent` changed type from `Instance` to `Polytoria.Datamodel.Instance`
- Method `IsDescendantOf` changed parameters: 
  - Parameter `parent` changed type from `Instance` to `Polytoria.Datamodel.Instance`
- Method `New` changed parameters: 
  - Parameter `parent` changed type from `Instance` to `Polytoria.Datamodel.Instance`
- Property `Item` in `InstanceProxy` changed type from `Instance` to `Polytoria.Datamodel.Instance`
- Property `Parent` in `InstanceProxy` changed type from `Instance` to `Polytoria.Datamodel.Instance`
- Property `ChildRemoved` in `InstanceProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `ChildAdded` in `InstanceProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Touched` in `InstanceProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `TouchEnded` in `InstanceProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Clicked` in `InstanceProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `MouseEnter` in `InstanceProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `MouseExit` in `InstanceProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## InstanceValueProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Property `Value` in `InstanceValueProxy` changed type from `Instance` to `Polytoria.Datamodel.Instance`
## LightingProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Property `AmbientSource` in `LightingProxy` changed type from `AmbientSource` to `Polytoria.Datamodel.AmbientSource`
## NetworkEventProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Method `InvokeServer` changed parameters: 
  - Parameter `msg` changed type from `NetMessage` to `Polytoria.Datamodel.NetMessage`
- Method `InvokeClient` changed parameters: 
  - Parameter `msg` changed type from `NetMessage` to `Polytoria.Datamodel.NetMessage`
  - Parameter `player` changed type from `Player` to `Polytoria.Datamodel.Player`
- Method `InvokeClients` changed parameters: 
  - Parameter `msg` changed type from `NetMessage` to `Polytoria.Datamodel.NetMessage`
- Property `InvokedServer` in `NetworkEventProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `InvokedClient` in `NetworkEventProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## NPCProxy
Inherits from: [DynamicInstanceProxy](#DynamicInstanceProxy)
- Property `Died` in `NPCProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `MoveTarget` in `NPCProxy` changed type from `Instance` to `Polytoria.Datamodel.Instance`
## ParticlesProxy
Inherits from: [DynamicInstanceProxy](#DynamicInstanceProxy)
- Property `ImageType` in `ParticlesProxy` changed type from `ImageType` to `Polytoria.Controllers.ImageType`
- Property `Color` in `ParticlesProxy` changed type from `ColorRange` to `Polytoria.Types.ColorRange`
- Property `ColorMode` in `ParticlesProxy` changed type from `ParticleColorMode` to `Polytoria.Datamodel.ParticleColorMode`
- Property `Lifetime` in `ParticlesProxy` changed type from `NumberRange` to `Polytoria.Types.NumberRange`
- Property `SizeOverLifetime` in `ParticlesProxy` changed type from `NumberRange` to `Polytoria.Types.NumberRange`
- Property `Speed` in `ParticlesProxy` changed type from `NumberRange` to `Polytoria.Types.NumberRange`
- Property `SimulationSpace` in `ParticlesProxy` changed type from `ParticleSimulationSpace` to `Polytoria.Datamodel.ParticleSimulationSpace`
- Property `StartRotation` in `ParticlesProxy` changed type from `NumberRange` to `Polytoria.Types.NumberRange`
- Property `AngularVelocity` in `ParticlesProxy` changed type from `NumberRange` to `Polytoria.Types.NumberRange`
- Property `Shape` in `ParticlesProxy` changed type from `ParticleShape` to `Polytoria.Datamodel.ParticleShape`
## PartProxy
Inherits from: [DynamicInstanceProxy](#DynamicInstanceProxy)
- Property `Shape` in `PartProxy` changed type from `PartShape` to `Polytoria.Datamodel.PartShape`
- Property `Material` in `PartProxy` changed type from `PartMaterial` to `Polytoria.Datamodel.PartMaterial`
## PlayerProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Method `OwnsItem` changed parameters: 
  - Parameter `callOnComplete` changed type from `MoonSharp.Interpreter.DynValue` to `MoonSharp.Interpreter.DynValue`
- Method `Sit` changed parameters: 
  - Parameter `seat` changed type from `Seat` to `Polytoria.Datamodel.Seat`
- Method `LookAt` changed parameters: 
  - Parameter `instance` changed type from `DynamicInstance` to `Polytoria.Datamodel.DynamicInstance`
- Property `SittingIn` in `PlayerProxy` changed type from `Seat` to `Polytoria.Datamodel.Seat`
- Property `Chatted` in `PlayerProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Died` in `PlayerProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Respawned` in `PlayerProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## PlayersProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Property `PlayerAdded` in `PlayersProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `PlayerRemoved` in `PlayersProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `LocalPlayer` in `PlayersProxy` changed type from `Player` to `Polytoria.Datamodel.Player`
## RemoveEventProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Method `Invoke` changed parameters: 
  - Parameter `val` changed type from `Instance` to `Polytoria.Datamodel.Instance`
- Property `Invoked` in `RemoveEventProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## SeatProxy
Inherits from: [PartProxy](#PartProxy)
- Property `Occupant` in `SeatProxy` changed type from `Player` to `Polytoria.Datamodel.Player`
- Property `Sat` in `SeatProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Vacated` in `SeatProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## SoundProxy
Inherits from: [DynamicInstanceProxy](#DynamicInstanceProxy)
- Property `Loaded` in `SoundProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## ToolProxy
Inherits from: [DynamicInstanceProxy](#DynamicInstanceProxy)
- Property `Activated` in `ToolProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Deactivated` in `ToolProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Equipped` in `ToolProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Unequipped` in `ToolProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## UIFieldProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Property `MouseUp` in `UIFieldProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `MouseDown` in `UIFieldProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## UIImageProxy
Inherits from: [UIFieldProxy](#UIFieldProxy)
- Property `ImageType` in `UIImageProxy` changed type from `ImageType` to `Polytoria.Controllers.ImageType`
## UITextInputProxy
Inherits from: [UIViewProxy](#UIViewProxy)
- Property `Changed` in `UITextInputProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Submitted` in `UITextInputProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## ValueBaseProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Property `Changed` in `ValueBaseProxy` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## AchievementServiceProxy
- Type removed
## CoreUIServiceProxy
- Type removed
## DatastoreProxy
- Type removed
## DataStoreServiceProxy
- Type removed
## InsertServiceProxy
- Type removed
## ScriptServiceProxy
- Type removed
