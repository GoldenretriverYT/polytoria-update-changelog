# Changes
## EnvironmentProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Method `RebuildNavMesh` changed parameters: 
  - Parameter `root` added
## MeshPartProxy
Inherits from: [PartProxy](#PartProxy)
- Method `PlayAnimation` changed parameters: 
  - Parameter `objectPath` added
  - Parameter `speed` added
  - Parameter `loop` added
- Method `StopAnimation` changed parameters: 
  - Parameter `name` added
- New method added: `GetAnimationSources` with parameters:
  - `animationName` of type `System.String`
- New method added: `GetAnimationInfo` with parameters:
- New property added: `PlayAnimationOnStart` of type ``System.Boolean``
- New property added: `CollisionType` of type ``Polytoria.Datamodel.CollisionType``
## NPCProxy
Inherits from: [DynamicInstanceProxy](#DynamicInstanceProxy)
- New method added: `EquipTool` with parameters:
  - `tool` of type `Polytoria.Datamodel.Tool`
- New method added: `DropTool` with parameters:
## SignalProxy
Inherits from: [InstanceProxy](#InstanceProxy)
Added new type: `SignalProxy`
- New method added: `Invoke` with parameters:
  - `par` of type `System.Object[]`
- New property added: `Invoked` of type ``Polytoria.Lua.LuaEvent``
## UIImageProxy
Inherits from: [UIFieldProxy](#UIFieldProxy)
- New property added: `Clickable` of type ``System.Boolean``
