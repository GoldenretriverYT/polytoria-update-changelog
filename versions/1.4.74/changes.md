# Changes
## DecalProxy
Inherits from: [DynamicInstanceProxy](#DynamicInstanceProxy)
- Property `ImageType` changed type from `ImageType` to `Polytoria.Controllers.ImageType`
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
- Property `Skybox` changed type from `SkyboxPreset` to `Polytoria.Datamodel.SkyboxPreset`
## GameProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Property `Rendered` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## InstanceProxy
Inherits from: [Object](#Object)
- Method `SetParent` changed parameters: 
  - Parameter `parent` changed type from `Instance` to `Polytoria.Datamodel.Instance`
- Method `IsDescendantOf` changed parameters: 
  - Parameter `parent` changed type from `Instance` to `Polytoria.Datamodel.Instance`
- Method `New` changed parameters: 
  - Parameter `parent` changed type from `Instance` to `Polytoria.Datamodel.Instance`
- Property `Item` changed type from `Instance` to `Polytoria.Datamodel.Instance`
- Property `Parent` changed type from `Instance` to `Polytoria.Datamodel.Instance`
- Property `ChildRemoved` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `ChildAdded` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Touched` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `TouchEnded` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Clicked` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `MouseEnter` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `MouseExit` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## InstanceValueProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Property `Value` changed type from `Instance` to `Polytoria.Datamodel.Instance`
## LightingProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Property `AmbientSource` changed type from `AmbientSource` to `Polytoria.Datamodel.AmbientSource`
## NetworkEventProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Method `InvokeServer` changed parameters: 
  - Parameter `msg` changed type from `NetMessage` to `Polytoria.Datamodel.NetMessage`
- Method `InvokeClient` changed parameters: 
  - Parameter `msg` changed type from `NetMessage` to `Polytoria.Datamodel.NetMessage`
  - Parameter `player` changed type from `Player` to `Polytoria.Datamodel.Player`
- Method `InvokeClients` changed parameters: 
  - Parameter `msg` changed type from `NetMessage` to `Polytoria.Datamodel.NetMessage`
- Property `InvokedServer` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `InvokedClient` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## NPCProxy
Inherits from: [DynamicInstanceProxy](#DynamicInstanceProxy)
- Property `Died` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `MoveTarget` changed type from `Instance` to `Polytoria.Datamodel.Instance`
## ParticlesProxy
Inherits from: [DynamicInstanceProxy](#DynamicInstanceProxy)
- Property `ImageType` changed type from `ImageType` to `Polytoria.Controllers.ImageType`
- Property `Color` changed type from `ColorRange` to `Polytoria.Types.ColorRange`
- Property `ColorMode` changed type from `ParticleColorMode` to `Polytoria.Datamodel.ParticleColorMode`
- Property `Lifetime` changed type from `NumberRange` to `Polytoria.Types.NumberRange`
- Property `SizeOverLifetime` changed type from `NumberRange` to `Polytoria.Types.NumberRange`
- Property `Speed` changed type from `NumberRange` to `Polytoria.Types.NumberRange`
- Property `SimulationSpace` changed type from `ParticleSimulationSpace` to `Polytoria.Datamodel.ParticleSimulationSpace`
- Property `StartRotation` changed type from `NumberRange` to `Polytoria.Types.NumberRange`
- Property `AngularVelocity` changed type from `NumberRange` to `Polytoria.Types.NumberRange`
- Property `Shape` changed type from `ParticleShape` to `Polytoria.Datamodel.ParticleShape`
## PartProxy
Inherits from: [DynamicInstanceProxy](#DynamicInstanceProxy)
- Property `Shape` changed type from `PartShape` to `Polytoria.Datamodel.PartShape`
- Property `Material` changed type from `PartMaterial` to `Polytoria.Datamodel.PartMaterial`
## PlayerProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Method `OwnsItem` changed parameters: 
  - Parameter `callOnComplete` changed type from `MoonSharp.Interpreter.DynValue` to `MoonSharp.Interpreter.DynValue`
- Method `Sit` changed parameters: 
  - Parameter `seat` changed type from `Seat` to `Polytoria.Datamodel.Seat`
- Method `LookAt` changed parameters: 
  - Parameter `instance` changed type from `DynamicInstance` to `Polytoria.Datamodel.DynamicInstance`
- Property `SittingIn` changed type from `Seat` to `Polytoria.Datamodel.Seat`
- Property `Chatted` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Died` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Respawned` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## PlayersProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Property `PlayerAdded` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `PlayerRemoved` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `LocalPlayer` changed type from `Player` to `Polytoria.Datamodel.Player`
## RemoveEventProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Method `Invoke` changed parameters: 
  - Parameter `val` changed type from `Instance` to `Polytoria.Datamodel.Instance`
- Property `Invoked` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## SeatProxy
Inherits from: [PartProxy](#PartProxy)
- Property `Occupant` changed type from `Player` to `Polytoria.Datamodel.Player`
- Property `Sat` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Vacated` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## SoundProxy
Inherits from: [DynamicInstanceProxy](#DynamicInstanceProxy)
- Property `Loaded` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## ToolProxy
Inherits from: [DynamicInstanceProxy](#DynamicInstanceProxy)
- Property `Activated` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Deactivated` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Equipped` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Unequipped` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## UIFieldProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Property `MouseUp` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `MouseDown` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## UIImageProxy
Inherits from: [UIFieldProxy](#UIFieldProxy)
- Property `ImageType` changed type from `ImageType` to `Polytoria.Controllers.ImageType`
## UITextInputProxy
Inherits from: [UIViewProxy](#UIViewProxy)
- Property `Changed` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
- Property `Submitted` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
## ValueBaseProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Property `Changed` changed type from `LuaEvent` to `Polytoria.Lua.LuaEvent`
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
