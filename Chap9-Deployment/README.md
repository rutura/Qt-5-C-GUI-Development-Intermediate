# Deploying a PySide6 Application

This lecture explains how to deploy a PySide6 application using the `pyside6-deploy` tool, with our painting application as an example.

## Overview of Deployment

Deploying a PySide6 application involves bundling your Python code, the PySide6 libraries, and any dependencies into a standalone package that can be distributed to users who don't have Python or PySide6 installed on their systems.

## Using pyside6-deploy

`pyside6-deploy` is a tool that simplifies the deployment process for PySide6 applications. It handles dependency detection and packaging in a single command.

### Basic Deployment Command

To deploy our painting application:

```bash
pyside6-deploy main.py
```

This command analyzes the application, identifies all dependencies, and creates the necessary files for distribution.

### Output Files

When running on Linux, `pyside6-deploy` generates:

1. **A `.spec` file**: This is a specification file that contains configuration for building the application.
2. **A `.bin` file**: This is the compiled executable version of your application.

On Windows, it would typically generate an `.exe` file, and on macOS, it would generate an `.app` bundle.

### Deployment Process

The tool follows these steps:
1. Analyzes the entry point (main.py) to identify imports
2. Collects all Python dependencies
3. Identifies PySide6 modules and resources
4. Bundles required Qt plugins and libraries
5. Generates a platform-specific executable

## Customizing Deployment

### Modifying the .spec File

The generated `.spec` file can be modified to customize the deployment:

```python
# Example .spec file modifications
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('translations/*.qm', 'translations')],  # Add translation files
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
```

After modifying the `.spec` file, you can rebuild the application using:

```bash
pyside6-deploy -f your_app.spec
```

### Common Customizations

- Adding resources (images, translations, etc.)
- Setting application icon
- Including additional libraries
- Excluding unnecessary modules
- Setting application metadata (name, version, author)

## Troubleshooting Deployment Issues

### Missing Dependencies

If your application depends on external libraries that aren't automatically detected:

```bash
pyside6-deploy main.py --hiddenimport=module_name
```

### Missing Resources

If resources are not included in the bundle:

```bash
pyside6-deploy main.py --add-data "path/to/resource:destination/in/bundle"
```

### Large Bundle Size

To reduce the size of the final executable:

```bash
pyside6-deploy main.py --exclude-module=unnecessary_module
```

## Distributing Your Application

### Linux Distribution

On Linux, distribute the `.bin` file. Users may need to:
1. Make the file executable: `chmod +x application.bin`
2. Run the application: `./application.bin`

### Creating an Installer (Optional)

For a more professional distribution, you can create an installer package:
- On Linux: Use tools like FPM, AppImage, or Flatpak
- On Windows: Use NSIS, Inno Setup, or similar
- On macOS: Create a DMG file or use macOS Installer

## Testing Deployment

Always test your deployed application on a clean system without Python or Qt installed to ensure it works correctly. Check for:

1. Missing dependencies
2. Resource loading issues
3. Platform-specific behaviors
4. Performance differences

## Deployment Best Practices

1. **Keep dependencies minimal**: Fewer dependencies mean smaller bundle size and fewer potential issues
2. **Test on target platforms**: Deploy and test on systems similar to your users'
3. **Version your releases**: Clear versioning helps with support and updates
4. **Include documentation**: Add a README or help file in your distribution
5. **Sign your application**: On macOS and Windows, sign your application to avoid security warnings

## Conclusion

Deploying PySide6 applications with `pyside6-deploy` streamlines the process of creating standalone executables that can run on systems without Python or Qt installed. This allows you to distribute your painting application to users regardless of their technical setup.

For our painting application with internationalization and undo/redo functionality, we've successfully deployed it into a standalone executable that maintains all features while being easy to distribute to end users.