# Database Tables

## Workshop Subsystem Tables
Virtual machine {
    id
    name
    file_name
    vrdp
    network adapters
    server id
    snapshots
    connection string
}

Workshop unit {
    id
    name
    description
    status
    lifetime
    published_date
    vms
    server id
    connection strings
    reference materials
    surveys
}

Workshop Group {
    id
    name
    description
    status
    lifetime
    published date
    wus
    server id
    reference materials
    surveys
}

Network adapter {
    id
    name
}


vm_adapters {
    virtual machine id
    network adapter id
}

units and reference materials {
    unit id
    reference material id
}

units and surveys {
    unit id
    survey id
}

group and reference materials {
    group id
    reference materials id
}

group and surveys {
    group id
    reference materials id
}

user workshop unit history {
    user id
    unit id
}

## User Subsystem 
User {
    id
    first name
    last name
    organization
    email
    skill_level
    credentials
    permissions
    workshop history
}

Credentials {
    username
    password
    salt
    user id
}

## Network Subsystem
Server {
    id
    ip
    credentials
    // Probably need to add the WGs, WUs, and VMs
}

Server Credentials {
    username
    password
    salt
    server id
}

Session {
    id
    user
    unit
    lifetime
    start time
}

Connection String {
    id
    file location
    vm id
    wu id // i don't think this one should be here
}

Statistics {
    id
    time stamp
    available
    used
    unused
    cpu
    memory
    server id
}

## Resource subsystem
Reference Materials {
    id
    name
    file location
    type
}

Survey {
    id
    name
    file location
    completed
    user who completed it
}